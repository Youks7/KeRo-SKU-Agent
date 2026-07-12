# Forward Run: sku-tiktok-shop

## Input preservation

Use the supplied `SKU_CONTEXT`, mode A. Test target: TikTok Shop US. Brand name, variations, included items, legal disclosures, and category-specific evidence are missing.

## Direction proposal

- A — PDP compliance: real front-view main image, then distinct real angles and details.
- B — Quick understanding: additional images for geometry, hinge, scale, included items, and use where policy allows.
- C — Content handoff: Shoppable Photo and video briefs kept separate from PDP main media.

Recommended: A+B for PDP; C as a separate content workstream.

## Confirmed production

| Asset | Task | Status |
| --- | --- | --- |
| PDP Main Image | real front physical view on required clean background | human-review |
| Additional front/side | distinct real angles | ready |
| Detail image | real hinge and frame transition | ready |
| Variation image | map each independent SKU | blocked |
| Shop Ads source check | confirm PDP facts and image match the sold SKU | human-review |
| Shoppable Photo brief | content-native use with separate policy review | direction-only |
| Video brief | handoff only | direction-only |

Main-image brief:

```text
Use the real front-view product image. Preserve the exact frame, dark lens color, bridge, hinge, and logo area. Use the required clean white background. Do not add text, logos, borders, watermarks, graphics, props, accessories, packaging, people, or digital product rendering.
```

## QA result

Pass: PDP, variations, Shop Ads source, Shoppable Photo, and video handoff were separated; unknown variations and disclosures remain blocked.

