# Forward Run: sku-taobao

## Input preservation

Use the supplied `SKU_CONTEXT`. Keep mode A. Do not claim lens performance, material, certification, dimensions, or included items.

## Direction proposal

- A — Search clarity: silhouette-led main media, then angle and hinge details. Best for fast product recognition.
- B — Styling imagination: restrained lifestyle backgrounds in carousel/detail slots only. Risk: model or face imagery can distract from unverified fit.
- C — Detail certainty: frame-to-temple transition and hinge close-ups, with editable text placeholders for later verified specs.

Recommended: A+C. It preserves search clarity while giving the detail page product-specific evidence.

## Confirmed production

| Slot | Task | Visual | Status |
| --- | --- | --- | --- |
| Main 1:1 or 3:4 | identify the sold SKU | real front-view cutout, clean background, no invented accessories | human-review |
| Carousel angle | show actual geometry | real 45-degree or side image, uncluttered negative space | ready |
| Carousel detail | prove product-specific construction | hinge close-up and frame-to-temple transition | ready |
| SKU property image | map each real color variant | one verified source image per attribute value | blocked until variants are supplied |
| Mobile detail modules | sequence identity, detail, use, verified specs | independent editable copy layers | human-review |

Representative background prompt:

```text
Create only a clean neutral studio background with soft directional light from upper left, subtle contact-shadow area reserved for a real black full-rim sunglasses cutout, generous mobile-safe negative space, no product, no glasses, no text, no logo, no packaging, no certification icons.
```

## QA result

Pass with conditions: the workflow separated main media, carousel, SKU images, and mobile modules; publication remains blocked for unsupplied variants and dimensions.

