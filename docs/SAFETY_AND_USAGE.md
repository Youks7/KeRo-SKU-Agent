# Safety And Usage Guide

KeRo SKU Skill is designed for real-SKU e-commerce workflows. It should help you plan product pages and prompts without inventing product facts.

V1.3 separates shared product evidence from marketplace production. Run `sku-product-core` once, preserve the resulting `SKU_CONTEXT`, and let each platform skill add only platform-specific fields.

## Core Safety Rules

- Do not invent product specifications.
- Do not invent material, certification, patent, claim, user review, sales number, or ranking.
- Do not alter the real SKU's color, structure, logo, packaging, or key details.
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

## Competitor References

Safe use:

- Composition rhythm
- Visual hierarchy
- Information structure
- General lighting or background direction

Unsafe use:

- Copying competitor products
- Copying logos or packaging
- Copying text
- Copying unique brand visual assets
- Presenting a similar product as the user's SKU

## Final Commercial QA

Before using any output commercially, check:

1. Product color and shape.
2. Logo and packaging text.
3. Material claims.
4. Functional claims.
5. Certification marks.
6. Size, weight, capacity, and compatibility.
7. CTA and promotional wording.
8. Platform policy compliance.

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
