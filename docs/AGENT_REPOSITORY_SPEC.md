# KeRo SKU Agent Repository Specification

## Objective

Create an independent `KeRo-SKU-Agent` repository by copying the existing `KeRo-SKU-skill` contents and adding a Codex custom Agent layer. The existing source repository must remain unchanged and must not receive any commits from this work.

## Requirements

1. Preserve the existing ten-Skill suite and its deterministic packages.
2. Add one project-scoped custom Agent named `kero-sku-director` under `.codex/agents/`.
3. Keep the Agent thin: it orchestrates Skills but does not duplicate marketplace rule bodies.
4. Require the Agent to preserve factual boundaries, reuse `SKU_CONTEXT`, wait for direction approval, report missing Skills, and keep project data outside installation directories.
5. Provide a Windows installer that installs the Agent and all ten Skills to the active Codex home.
6. The installer must be idempotent, refuse silent overwrite, and back up conflicts before an explicitly forced update.
7. Avoid hard-coded Chinese source paths in the PowerShell installer so Windows PowerShell 5.1 can run it reliably.
8. Add a static validator and a declarative behavior contract covering routing, state reuse, approval gates, missing dependencies, multi-platform behavior, and project-file isolation.
9. Run the Agent validator in GitHub Actions and during deterministic package builds.
10. Document installation, invocation, capability boundaries, update behavior, and recommended SKU project storage.
11. Create and push only to the new GitHub repository. Keep the old repository configured as read-only upstream context locally.

## Acceptance Criteria

- `python scripts/validate_agent.py` passes.
- Every existing validation script used by CI passes.
- `python scripts/build_skill_packages.py` succeeds and package validation passes afterward.
- The installer succeeds in a clean temporary Codex home.
- Running the installer twice reports all components as current.
- A conflicting installed Agent is rejected without `-Force`.
- With `-Force`, the conflict is backed up before replacement.
- `git diff --check` reports no whitespace errors.
- The final Git remote named `origin` points to `Youks7/KeRo-SKU-Agent`; the original repository is never pushed.
