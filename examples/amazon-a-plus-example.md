# Example: Amazon A+ Workflow

## Scenario

You need Amazon listing images or A+ modules from real product images.

## Starter Prompt

```text
Use $sku-detail-page-director to analyze the uploaded product images.

Target platform: Amazon
Output language: English
Expected deliverable: listing images and A+ modules
Core selling points: not confirmed yet; infer cautiously from visible evidence

Start with Stage 1.
Do not create final image-generation prompts until I approve a direction.
Do not invent unverified material, dimensions, certification, function, review, rating, or compatibility.
```

## Stage 1 Should Clarify

- What the product appears to be.
- Which facts are visible.
- Which facts require documents.
- Recommended product-handling mode.
- Amazon-specific visual risks.
- What decision is needed next.

## Direction Reply Example

```text
Choose the recommended listing-clarity direction.
Use strict fidelity for the Main Image and keep lifestyle or benefit content in eligible secondary/A+ modules.
Do not unlock blocked dimensions, included items, brand claims, or performance claims.
```

## Stage 3 Prompt

```text
Create only the Listing Image and A+ units supported by the target marketplace, category, brand role, and current Seller Central access.
Do not invent a fixed module count or slice a generic long image into A+.
For every confirmed unit, provide source evidence, sales objective, composition, handling mode, prompt, negative prompt, copy placement, post-layout, shot matrix, and product-fidelity checks.
```

## Amazon Notes

- Avoid unsupported claims.
- Do not invent certifications.
- Keep product identity consistent.
- Use post-production for final copy and icons.
- Check Amazon category rules before publication.
