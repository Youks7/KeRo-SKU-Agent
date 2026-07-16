# Changelog

All notable changes to this repository are documented here.

## v1.4.0-dev

- Reframed fidelity from global source-pixel reuse to an explicit SKU identity contract.
- Added progressive intake, product-image diagnosis, multi-view confidence, reference-page semantic segmentation, reference abstraction, and breakpoint resume.
- Added `SKU_CONTEXT V2`, `IDENTITY_CONTRACT`, and `CREATIVE_CONTEXT`.
- Replaced global Mode A/B/C with per-asset-slot F0 evidence, F1 pixel-preserving composite, F2 identity-conditioned reconstruction, and F3 concept exploration.
- Required three creative directions that differ in at least three of five dimensions: thesis, visual world, product role, camera/light, and narrative arc.
- Added strict, controlled, and free creative opportunity maps for all eight marketplace skills.
- Added planning—prompt—generation separation, creative-quality and reference-rights gates, and an identity-anchored sunglasses regression.
- Made `SKU_CONTEXT.json` the single authoritative persisted state, with revision precedence, atomic write-back guidance, and an executable stale-index recovery test.
- Added persisted per-platform contexts, active-platform selection, and executable fallback to the first unfinished unit when `resume_from` is empty.
- Made resume resolution stage-gated so prefilled production units cannot bypass direction approval.
- Added an external real-sunglasses multi-view input validator and regression record without committing private product images; F2 outputs remain human-reviewed.
- Expanded the F1 regression from a flat gray background to architectural lighting, environment color matching, contact shadows, perspective, edge spill, and repair routing.
- Closed single-image F2 routing and made `repair-required` part of the canonical per-unit release-state set.

## v0.1.0-agent

- Created an independent KeRo SKU Agent repository from the existing Skill suite while leaving the source repository unchanged.
- Added the `kero-sku-director` custom Agent as a thin orchestration layer over all ten Skills.
- Added a conflict-safe Windows installer with idempotence checks and timestamped backups before forced updates.
- Added a static Agent validator and seven-scenario behavioral contract covering routing, approval gates, recovery, and project-file isolation.
- Added Agent documentation, invocation examples, storage guidance, and CI validation.

## v1.3.0-dev

- Converted the compatibility router into a true one-entry workflow that continues through product-core and marketplace direction stages without asking users to invoke multiple Skills manually.
- Removed the Mode A/B Prompt collision: Mode A now generates a product-free background layer, while Mode B preserves existing Logo, label, packaging text, and product identity without banning those elements as bare negative tokens.
- Made the full production protocol stage-conditional, consolidated canonical shared sources, added stale-package cleanup, and added GitHub Actions validation.
- Restored the Lite V1.2.1 full per-screen production depth as a mandatory per-unit protocol across all eight marketplace skills, including Prompt, Negative Prompt, handling mode, copy placement, post-layout, shot matrix, product-fidelity QA, and generic-Prompt interception.
- Added page-level visual tokens, cross-unit continuity, evidence binding, publication states, canonical protocol synchronization, and automated regression validation without forcing non-long-page platforms into fixed screen counts.
- Replaced the all-platform monolith with a compatibility router, a shared product-fact core, and eight marketplace-specific skills.
- Added a versioned `SKU_CONTEXT` for one-time product analysis and multi-platform handoff.
- Added standalone Taobao, Tmall, Pinduoduo, JD, 1688, Amazon, Shopify, and TikTok Shop workflows.
- Added canonical safety-rule synchronization, structure validation, trigger-test corpora, asset validation, deterministic package builds, and SHA-256 manifests.
- Updated the legacy `.skill` path to contain the compatibility router.
- Preserved Lite V1.2.1 as the baseline Git tag.

## v1.2.1

- Added anti-homogenization production rules.
- Added the three-stage SKU detail-page workflow.
- Added product-fidelity modes for strict fidelity, AI-assisted product images, and concept generation.
- Added competitor-reference safety rules.
- Added per-screen prompt production logic.
- Added product consistency QA requirements.

## Repository Packaging

- Added installation guidance.
- Added troubleshooting documentation.
- Added safety and usage guidance.
- Added example workflows.
- Added GitHub issue and pull request templates.
- Added optional static website files.
- Added repository social preview asset.
