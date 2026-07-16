# KeRo SKU Agent Repository Specification

## Objective

Create an independent `KeRo-SKU-Agent` repository by copying the existing `KeRo-SKU-skill` contents and adding a Codex custom Agent layer. The existing source repository must remain unchanged and must not receive any commits from this work.

## Requirements

1. Preserve the existing ten-Skill suite, add `sku-reference-migration`, and build deterministic packages for all eleven Skills.
2. Add one project-scoped custom Agent named `kero-sku-director` under `.codex/agents/`.
3. Keep the Agent thin: it orchestrates Skills but does not duplicate marketplace rule bodies.
4. Require the Agent to preserve factual boundaries, reuse `SKU_CONTEXT`, wait for direction approval, report missing Skills, and keep project data outside installation directories.
5. Provide a Windows installer that installs the Agent and all eleven Skills to the active Codex home.
6. The installer must be idempotent, refuse silent overwrite, and back up conflicts before an explicitly forced update.
7. Avoid hard-coded Chinese source paths in the PowerShell installer so Windows PowerShell 5.1 can run it reliably.
8. Add a static validator and a declarative behavior contract covering routing, state reuse, approval gates, missing dependencies, multi-platform behavior, and project-file isolation.
9. Run the Agent validator in GitHub Actions and during deterministic package builds.
10. Document installation, invocation, capability boundaries, update behavior, and recommended SKU project storage.
11. Create and push only to the new GitHub repository. Keep the old repository configured as read-only upstream context locally.
12. Diagnose product images and unify multi-view evidence before creative production.
13. Add `IDENTITY_CONTRACT` and `CREATIVE_CONTEXT` while preserving V1 `SKU_CONTEXT` facts during migration.
14. Replace global Mode A/B/C routing with per-slot F0–F3 modes.
15. Segment reference detail pages semantically and store a reference-abstraction report instead of copying competitor assets.
16. Require three directions that differ in at least three creative dimensions, then separate planning, prompt extraction, and generation.
17. Preserve workflow state for breakpoint resume using one authoritative `SKU_CONTEXT.json`, explicit revision precedence, and recovery validation.
18. Add an identity-anchored sunglasses regression plus an external real-SKU input gate that never commits private product images.
19. Add semantic reference-page segmentation, rights status, M1/M2/M3 modes, evidence-bound module mapping, three migration directions, cross-platform remapping, and breakpoint resume in one authoritative `SKU_CONTEXT.json`.

## Acceptance Criteria

- `python scripts/validate_agent.py` passes.
- Every existing validation script used by CI passes.
- `python scripts/build_skill_packages.py` succeeds and package validation passes afterward.
- The installer succeeds in a clean temporary Codex home.
- Running the installer twice reports all components as current.
- A conflicting installed Agent is rejected without `-Force`.
- With `-Force`, the conflict is backed up before replacement.
- `git diff --check` reports no whitespace errors.
- `python scripts/validate_creative_system.py` passes.
- `python scripts/validate_resume_state.py` resolves the authoritative state and ignores a stale optional index.
- `python scripts/validate_production_protocol.py` passes with the sunglasses F2 fixture.
- `python scripts/validate_reference_migration.py` passes with authorized M2, competitor M3, Taobao-to-Amazon remap, and direction-gate fixtures.
- A user-authorized external front, three-quarter, and back sunglasses fixture passes `validate_real_sku_fixture.py`; this does not replace generated-image identity review.
- The final Git remote named `origin` points to `Youks7/KeRo-SKU-Agent`; the original repository is never pushed.
