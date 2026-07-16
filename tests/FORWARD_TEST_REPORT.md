# KeRo SKU Skills Forward Test Report

## V1.4 real-sunglasses direction-gate forward test

Test date: 2026-07-16

Execution: independent read-only agent session, no expected answer supplied

Input: three user-authorized external images of one white-frame, smoke-gradient-lens sunglasses SKU; private images stayed outside the repository
Target: Taobao mobile detail, stopping at direction confirmation

Result: **PASS WITH OUTPUT-FIDELITY LIMITATION**.

- Diagnosed the images instead of treating their filenames as truth. In particular, it corrected the third image from a claimed standard back view to a rear/temple-folded view and kept hidden hinge and inner-temple structure unknown.
- Established evidence boundaries and an `IDENTITY_CONTRACT` around the frame/lens silhouette, wide bridge, white frame, smoke gradient, ring ornament, horizontal connector, diamond-pattern temple, and curved temple tip.
- Refused to infer material, gemstone type, optical performance, dimensions, brand, model, fit, packaging, certification, or price.
- Proposed three directions—identity evidence board, ring-to-diamond detail chain, and urban-wear transition—that differed across thesis, visual world, product role, camera/light, and narrative arc.
- Routed proof slots to F0, pixel-preserving environments to F1, new-view/wear scenes to F2 `human-review`, and concept work to F3 `direction-only`.
- Stopped before formal production Prompt because no direction had been selected.

The test found no contract-level failure. It did identify real production constraints: the supplied source may be strongly retouched or rendered; white-on-white extraction risks edge loss; dimensions and optical claims are unavailable; the folded rear view does not prove hidden structure. No actual image-generation tool was run, so this test does not prove F2 output fidelity.

## V1.4 deterministic addendum

- `SKU_CONTEXT V2`, `IDENTITY_CONTRACT`, `CREATIVE_CONTEXT`, F0–F3, reference abstraction, and breakpoint resume are statically validated.
- All eight platform skills declare strict, controlled, and free creative slots.
- The sunglasses direction fixture requires three directions that differ across thesis, visual world, product role, camera/light, and narrative arc.
- The F2 sunglasses fixture binds front, side, and hinge evidence and remains `human-review` until identity landmarks pass.
- `validate_resume_state.py` proves that the authoritative `SKU_CONTEXT.json` wins over a stale optional index.
- `validate_real_sku_fixture.py` passed three external 1448×1086 views with independent hashes without copying them into the repository.
- These checks prove the current contracts, input integrity, and one independent direction-gate execution—not actual image-generation fidelity on every model.

## V1.3 historical report

Test date: 2026-07-12  
Branch: `codex/multi-platform-skills-v1.3`

## Scope

This report covers the eight platform skills: Taobao, Tmall, Pinduoduo, JD, 1688, Amazon, Shopify, and TikTok Shop.

All workflows used the same sanitized sunglasses `SKU_CONTEXT`. The fixture intentionally omits dimensions, materials, lens-performance evidence, prices, variants, brand rights, package contents, warranty, production capacity, and B2B commercial terms so evidence gating can be tested.

## Execution layers

| Layer | Result | Evidence |
| --- | --- | --- |
| Codex skill discovery in a fresh isolated `CODEX_HOME` | PASS | All 10 suite skills appeared in `codex debug prompt-input`; none missing |
| Skill structure and local references | PASS | `validate_all_skills.py` |
| Standalone package/source equivalence | PASS | `validate_packages.py` |
| Static trigger corpus | PASS | 100 positive and 50 negative cases |
| Single-agent full platform workflow execution | PASS WITH LIMITATION | Eight recorded direction-to-final runs under `tests/forward-runs/` |
| Clean cloud-backed Codex sessions | NOT VERIFIED | CLI device login was blocked by the restricted network environment |

## Platform results

| Skill | Direction stage | Final stage | Required evidence gating | Result |
| --- | --- | --- | --- | --- |
| `sku-taobao` | Distinct search-clarity, styling, and detail directions | Main media, carousel, SKU image, mobile modules | Variants and dimensions blocked | PASS |
| `sku-tmall` | Brand-system, construction, and lifestyle directions | Brand media, SPU/SKU, detail, story, qualification | Brand rights, assets, SPU/SKU, qualifications blocked | PASS |
| `sku-pinduoduo` | SKU certainty, visible value, and use directions | Exposure, carousel, SKU and detail plan | Price, delivery contents, variants blocked | PASS |
| `sku-jd` | Parameter, fit/use, and service directions | Parameter matrix, compatibility, packaging, service modules | Dimensions, performance, package, warranty blocked | PASS |
| `sku-1688` | Purchasing, customization, and sample workflow directions | Procurement, MOQ, price, OEM/ODM, production, logistics modules | All missing B2B terms blocked | PASS |
| `sku-amazon` | Listing clarity, fit/scale, and lifestyle directions | Main Image, secondary images, video brief, A+ structure | ASIN/brand role, dimensions, included items, performance blocked | PASS |
| `sku-shopify` | Conversion, editorial, and education directions | Responsive PDP sections, media, variants, metafields, SEO, CTA | Commerce, policy and specification fields blocked | PASS |
| `sku-tiktok-shop` | PDP compliance, quick understanding, and content handoff | PDP, variation, Shop Ads source, Shoppable Photo, video brief | Variations, disclosures and category evidence blocked | PASS |

## Safety observations

- No platform output asserted polarization, UV protection, certification, specific material, dimensions, price, MOQ, factory capacity, warranty, or included items.
- Mode A remained unchanged across all eight platforms.
- Taobao did not force every asset into 9:16.
- Pinduoduo refused exposure approval without a SKU-price-image matrix.
- 1688 did not invent B2B commercial or factory data.
- Amazon separated Main Image, secondary images, and A+.
- Shopify produced semantic PDP sections and a real CTA requirement instead of fixed image screens.
- TikTok Shop separated PDP media from Shoppable Photo and video content.

## Limitation

The eight platform outputs were executed sequentially by one agent with a shared fixture. They validate workflow logic and output differentiation, but they do not prove implicit invocation or multi-turn state retention in eight independent clean model sessions.

At that V1.3 test point, the release remained `v1.3.0-dev` pending clean-session testing. V1.4 now adds one independent real-product direction-gate test, while actual F2 generated-output fidelity remains a separate unresolved production check.

## Per-unit production protocol addendum

After the initial forward runs, the full Lite V1.2.1 per-screen production depth was restored as a canonical platform-aware protocol. All eight marketplace skills now require every screen, asset slot, A+ module, or media-bearing PDP section to preserve Prompt, Negative Prompt, handling mode, copy placement, post-layout, shot matrix, product-consistency QA, and generic-Prompt interception.

Deterministic validation confirms that all eight skills carry an identical canonical protocol and reference it directly. Taobao image-production and Shopify semantic-component regression fixtures pass. The original eight recorded model outputs predate this contract, so clean independent model sessions must still be rerun before the addendum is considered model-level validation.

## Usability-cleanup addendum

The one-entry director, stage-gated production loading, and distinct Mode A/Mode B Prompt contracts are now covered by deterministic validators. Mode A background generation no longer receives product-identity descriptions; Mode B preserves existing Logo, label, and packaging text without banning those elements as bare negative tokens. A dedicated Mode B reference-edit fixture and orchestration validator pass.

These checks prevent known instruction collisions and packaging drift, but they remain static regressions. The eight historical platform records below predate the usability cleanup and must not be presented as proof that a clean model session followed the new one-entry flow or the new mode-specific contracts.
