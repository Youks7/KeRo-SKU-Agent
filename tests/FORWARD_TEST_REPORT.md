# KeRo SKU Skills V1.3 Forward Test Report

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

Production release should therefore remain `v1.3.0-dev` until clean-session testing is completed with an authenticated Codex CLI or equivalent isolated sessions and at least one authorized real-product fixture.

## Per-unit production protocol addendum

After the initial forward runs, the full Lite V1.2.1 per-screen production depth was restored as a canonical platform-aware protocol. All eight marketplace skills now require every screen, asset slot, A+ module, or media-bearing PDP section to preserve Prompt, Negative Prompt, handling mode, copy placement, post-layout, shot matrix, product-consistency QA, and generic-Prompt interception.

Deterministic validation confirms that all eight skills carry an identical canonical protocol and reference it directly. Taobao image-production and Shopify semantic-component regression fixtures pass. The original eight recorded model outputs predate this contract, so clean independent model sessions must still be rerun before the addendum is considered model-level validation.
