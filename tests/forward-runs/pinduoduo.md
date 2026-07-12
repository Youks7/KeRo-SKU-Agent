# Forward Run: sku-pinduoduo

## Input preservation

Use the supplied `SKU_CONTEXT`, mode A. SKU prices, quantities, bundles, gifts, and included items are not available.

## Direction proposal

- A — SKU certainty: exposure image and variant images are generated only after price and delivery mapping.
- B — Visible-value proof: use real angles and hinge detail instead of unsupported performance claims.
- C — Quick-use understanding: simple wearing-context handoff for later content assets, not the exposure image.

Recommended: A+B. Price/SKU certainty is mandatory before exposure production.

## SKU—price—image matrix

| SKU | Price | Delivered items | Source image | Exposure eligible |
| --- | --- | --- | --- | --- |
| pending | pending | pending | pending | no |

## Confirmed production

| Slot | Task | Status |
| --- | --- | --- |
| Exposure image | show the exact purchasable SKU | blocked until lowest-price SKU is known |
| Carousel identity | front and side views of real SKU | ready |
| Carousel detail | hinge and frame transition | ready |
| SKU image | match color/package/quantity | blocked until all variants are supplied |
| Detail image | explain visible structure and delivery contents | blocked on included-item list |

Representative prompt:

```text
Create only a bright clean background for a verified real-product cutout, reserved area for the exact sold SKU and later editable specification copy, no product generation, no promotional badge, no subsidy mark, no platform logo, no gift, no extra case, no text.
```

## QA result

Pass by refusing misleading production: the skill detected that exposure media cannot be approved without SKU, price, quantity, and delivery mapping.

