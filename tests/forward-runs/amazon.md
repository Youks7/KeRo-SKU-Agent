# Forward Run: sku-amazon

## Input preservation

Use the supplied `SKU_CONTEXT`, mode A. Test target: Amazon US. ASIN, brand role, dimensions, included items, and lens-performance evidence are missing.

## Direction proposal

- A — Listing clarity: compliant real-product Main Image plus non-repeating angle/detail secondary images.
- B — Fit and scale confidence: use only after dimensions or a verified scale reference is supplied.
- C — Lifestyle context: restrained secondary image or A+ module, never the Main Image.

Recommended: A now; add B after dimension evidence.

## Confirmed production

| Asset | Task | Status |
| --- | --- | --- |
| Main Image | exact sold product on required clean background | human-review |
| Secondary 1 | real side/45-degree geometry | ready |
| Secondary 2 | hinge and frame transition detail | ready |
| Secondary 3 | included items | blocked |
| Secondary 4 | dimensions/fit | blocked |
| A+ modules | details, use, brand story, comparison | blocked on brand role and evidence |

Main-image brief:

```text
Use the real front-view sunglasses image as the only product identity. Preserve frame geometry, lens color, hinge, bridge, and logo area. Place the real cutout on a pure clean background with even lighting and natural edge quality. Do not add text, badges, props, accessories, packaging, or a second product.
```

Secondary background prompt:

```text
Generate only a neutral studio background with controlled side lighting and a macro-detail area reserved for the real hinge crop, no product, no text, no logo, no performance icons, no certification badge.
```

## QA result

Pass: Main Image and secondary/A+ systems were separated; unavailable evidence correctly blocked fit, included-item, brand, and lens-performance content.

