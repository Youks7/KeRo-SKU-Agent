# Safety And Usage Guide

KeRo SKU Skill is designed for real-SKU e-commerce workflows. It should help you plan product pages and prompts without inventing product facts.

V1.5 separates product truth, reference method, and final presentation. Run `sku-product-core` once, preserve `SKU_CONTEXT V2` and the `IDENTITY_CONTRACT`, then use `sku-reference-migration` when a reference page is supplied. The director stores `REFERENCE_MIGRATION_CONTEXT`, creates a reusable `CREATIVE_CONTEXT`, and assigns F0–F3 per marketplace asset slot.

## Core Safety Rules

- Do not invent product specifications.
- Do not invent material, certification, patent, claim, user review, sales number, or ranking.
- Lock the real SKU's identity; do not treat the source pixels as the only possible composition.
- Do not alter the real SKU's color, structure, proportions, logo, packaging, or key details.
- Do not copy competitor product designs, logos, text, packaging, or brand assets.
- Do not treat AI-generated images as final commercial assets without human QA.
- Do not let a platform skill overwrite verified product facts or upgrade an inference without new evidence.
- Check the current marketplace, region, category, and asset-slot rules before publication.

## Product Facts

Only treat information as fact when it is:

- Clearly visible in the image.
- Explicitly provided by the user.
- Confirmed by product documents.

If something is uncertain, label it as uncertain or avoid using it.

## Fidelity And Creative Freedom

- F0 uses a real photograph or faithful retouch for evidence-sensitive slots.
- F1 preserves real product pixels while rebuilding the scene, light, shadow, material world, and layout.
- F2 uses multiple verified views, masks, and identity landmarks for controlled new views or wearing scenes; it always requires human identity review.
- F3 is concept-only and cannot be published as a real-SKU asset.

Choose the mode per asset slot. A strict main image does not force secondary images, A+, PDP sections, or approved detail modules to reuse the same cutout.

## Competitor References

Safe use after semantic segmentation and a reference-abstraction report:

- Composition rhythm
- Visual hierarchy
- Information structure
- General lighting or background direction
- Camera grammar, material language, information density, and narrative rhythm

Unsafe use:

- Copying competitor products
- Copying logos or packaging
- Copying text
- Copying unique brand visual assets
- Presenting a similar product as the user's SKU
- Copying a unique campaign symbol, person identity, or one-to-one module layout

### Reference migration modes

- M1 structure migration reuses purchasing questions, module roles, and narrative order while redesigning the visual expression.
- M2 visual-language migration is limited to self-owned or explicitly authorized pages. It reuses abstract composition, camera, light, material, and graphic grammar, never source-product facts.
- M3 creative reinterpretation keeps only the commercial problem and emotional goal, then creates a different visual world. Use it by default for competitor or unknown sources.

Every non-discarded target module must bind to real SKU evidence. Target marketplace rules override source-page dimensions, module counts, overlays, and publishing behavior.

## Final Commercial QA

Before using any output commercially, check:

1. Product identity landmarks, color, shape, and view evidence.
2. Logo and packaging text.
3. Material claims.
4. Functional claims.
5. Certification marks.
6. Size, weight, capacity, and compatibility.
7. CTA and promotional wording.
8. Platform policy compliance.
9. Creative direction distinctness and reference-copying risk.

## High-Risk Categories

Use extra caution for:

- Medical and health products
- Beauty and skincare
- Food and supplements
- Baby products
- Safety equipment
- Electrical appliances
- Protective gear

These categories require stricter human review before publication.
