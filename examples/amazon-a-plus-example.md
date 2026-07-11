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
Choose B.
Use a clean Amazon-friendly style.
Keep the product accurate and avoid exaggerated claims.
```

## Stage 3 Prompt

```text
Create 6 Amazon modules based on the approved direction.
Choose aspect ratio by module purpose.
Do not force every image into 9:16.
Before each module, provide the sales objective, composition, prompt, negative prompt, and product-fidelity checks.
```

## Amazon Notes

- Avoid unsupported claims.
- Do not invent certifications.
- Keep product identity consistent.
- Use post-production for final copy and icons.
- Check Amazon category rules before publication.
