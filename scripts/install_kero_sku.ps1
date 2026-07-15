[CmdletBinding()]
param(
    [string]$CodexHome,
    [switch]$Force
)

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $PSScriptRoot

if (-not $CodexHome) {
    $CodexHome = if ($env:CODEX_HOME) {
        $env:CODEX_HOME
    } else {
        Join-Path $HOME ".codex"
    }
}

$agentSource = Join-Path $repoRoot ".codex\agents\kero-sku-director.toml"
$agentDirectory = Join-Path $CodexHome "agents"
$agentDestination = Join-Path $agentDirectory "kero-sku-director.toml"
$skillsDirectory = Join-Path $CodexHome "skills"

$routerCandidates = @(
    Get-ChildItem -LiteralPath $repoRoot -Directory |
        ForEach-Object { Join-Path $_.FullName "sku-detail-page-director" } |
        Where-Object { Test-Path -LiteralPath (Join-Path $_ "SKILL.md") -PathType Leaf }
)
if ($routerCandidates.Count -ne 1) {
    throw "Expected exactly one sku-detail-page-director source; found $($routerCandidates.Count)."
}
$routerSource = $routerCandidates[0]

$skillSources = @(
    [pscustomobject]@{
        Name = "sku-detail-page-director"
        Source = $routerSource
    },
    [pscustomobject]@{ Name = "sku-product-core"; Source = Join-Path $repoRoot "skills\sku-product-core" },
    [pscustomobject]@{ Name = "sku-taobao"; Source = Join-Path $repoRoot "skills\sku-taobao" },
    [pscustomobject]@{ Name = "sku-tmall"; Source = Join-Path $repoRoot "skills\sku-tmall" },
    [pscustomobject]@{ Name = "sku-pinduoduo"; Source = Join-Path $repoRoot "skills\sku-pinduoduo" },
    [pscustomobject]@{ Name = "sku-jd"; Source = Join-Path $repoRoot "skills\sku-jd" },
    [pscustomobject]@{ Name = "sku-1688"; Source = Join-Path $repoRoot "skills\sku-1688" },
    [pscustomobject]@{ Name = "sku-amazon"; Source = Join-Path $repoRoot "skills\sku-amazon" },
    [pscustomobject]@{ Name = "sku-shopify"; Source = Join-Path $repoRoot "skills\sku-shopify" },
    [pscustomobject]@{ Name = "sku-tiktok-shop"; Source = Join-Path $repoRoot "skills\sku-tiktok-shop" }
)

function Get-DirectoryFingerprint {
    param([Parameter(Mandatory)][string]$Path)

    $resolved = (Resolve-Path -LiteralPath $Path).Path
    $entries = Get-ChildItem -LiteralPath $resolved -Recurse -File |
        Sort-Object FullName |
        ForEach-Object {
            $relative = $_.FullName.Substring($resolved.Length).TrimStart("\", "/")
            $hash = (Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash
            "$relative|$hash"
        }
    $payload = [Text.Encoding]::UTF8.GetBytes(($entries -join "`n"))
    $algorithm = [Security.Cryptography.SHA256]::Create()
    try {
        return ([BitConverter]::ToString($algorithm.ComputeHash($payload))).Replace("-", "")
    } finally {
        $algorithm.Dispose()
    }
}

if (-not (Test-Path -LiteralPath $agentSource -PathType Leaf)) {
    throw "Missing Agent source: $agentSource"
}
foreach ($skill in $skillSources) {
    $skillFile = Join-Path $skill.Source "SKILL.md"
    if (-not (Test-Path -LiteralPath $skillFile -PathType Leaf)) {
        throw "Missing Skill source: $skillFile"
    }
}

$operations = @()
$agentState = "install"
if (Test-Path -LiteralPath $agentDestination -PathType Leaf) {
    $sourceHash = (Get-FileHash -LiteralPath $agentSource -Algorithm SHA256).Hash
    $destinationHash = (Get-FileHash -LiteralPath $agentDestination -Algorithm SHA256).Hash
    $agentState = if ($sourceHash -eq $destinationHash) { "current" } else { "conflict" }
}
$operations += [pscustomobject]@{
    Kind = "Agent"
    Name = "kero-sku-director"
    Source = $agentSource
    Destination = $agentDestination
    State = $agentState
}

foreach ($skill in $skillSources) {
    $destination = Join-Path $skillsDirectory $skill.Name
    $state = "install"
    if (Test-Path -LiteralPath $destination -PathType Container) {
        $state = if ((Get-DirectoryFingerprint $skill.Source) -eq (Get-DirectoryFingerprint $destination)) {
            "current"
        } else {
            "conflict"
        }
    }
    $operations += [pscustomobject]@{
        Kind = "Skill"
        Name = $skill.Name
        Source = $skill.Source
        Destination = $destination
        State = $state
    }
}

$conflicts = @($operations | Where-Object State -eq "conflict")
if ($conflicts.Count -gt 0 -and -not $Force) {
    $details = ($conflicts | ForEach-Object { "- $($_.Kind) $($_.Name): $($_.Destination)" }) -join "`n"
    throw "Existing installations differ from this repository. No files were changed.`n$details`nRerun with -Force to back up and replace them."
}

New-Item -ItemType Directory -Path $agentDirectory -Force | Out-Null
New-Item -ItemType Directory -Path $skillsDirectory -Force | Out-Null

$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
$backupRoot = Join-Path $CodexHome "backups\kero-sku\$timestamp"
if ($conflicts.Count -gt 0) {
    New-Item -ItemType Directory -Path $backupRoot -Force | Out-Null
}

foreach ($operation in $operations) {
    if ($operation.State -eq "current") {
        Write-Host "Current: $($operation.Kind) $($operation.Name)"
        continue
    }

    if ($operation.State -eq "conflict") {
        $backupDestination = Join-Path $backupRoot "$($operation.Kind.ToLowerInvariant())s\$($operation.Name)"
        New-Item -ItemType Directory -Path (Split-Path -Parent $backupDestination) -Force | Out-Null
        Move-Item -LiteralPath $operation.Destination -Destination $backupDestination
        Write-Host "Backed up: $backupDestination"
    }

    if ($operation.Kind -eq "Agent") {
        Copy-Item -LiteralPath $operation.Source -Destination $operation.Destination
    } else {
        Copy-Item -LiteralPath $operation.Source -Destination $operation.Destination -Recurse
    }
    Write-Host "Installed: $($operation.Kind) $($operation.Name)"
}

$missing = @()
if (-not (Test-Path -LiteralPath $agentDestination -PathType Leaf)) {
    $missing += $agentDestination
}
foreach ($skill in $skillSources) {
    $installedSkill = Join-Path $skillsDirectory "$($skill.Name)\SKILL.md"
    if (-not (Test-Path -LiteralPath $installedSkill -PathType Leaf)) {
        $missing += $installedSkill
    }
}
if ($missing.Count -gt 0) {
    throw "Installation verification failed:`n$($missing -join "`n")"
}

Write-Host "KeRo SKU Agent installation verified."
Write-Host "Agent: $agentDestination"
Write-Host "Skills: $skillsDirectory"
Write-Host "Start a new Codex task. Restart Codex only if the Agent is not discovered."
