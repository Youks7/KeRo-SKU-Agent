# Forward Run: sku-shopify

## Input preservation

Use the supplied `SKU_CONTEXT`, mode A. Test target: English-language Shopify PDP. Theme, variants, prices, inventory, shipping, returns, dimensions, and brand copy are missing.

## Direction proposal

- A — Conversion-first PDP: product identity, real gallery, variant selector, verified benefits, details, FAQ, shipping/returns, and real Add to Cart.
- B — Editorial detail: larger real-product media and craftsmanship sections while keeping critical information in HTML.
- C — Education-first: fit, care, dimensions, and lens information only after evidence arrives.

Recommended: A+B. Use real HTML content and responsive media, not an eight-image long page.

## Confirmed PDP map

| Section | Content | Status |
| --- | --- | --- |
| Hero | real product gallery, title, price, variants, Add to Cart | blocked on commerce fields |
| Product media | front, side, hinge, packaging | human-review |
| Visible details | frame transition and hinge | ready |
| Specifications | metafield-driven values | blocked |
| FAQ | verified fit, care, shipping, returns | blocked |
| Trust/brand | real policies and brand evidence | blocked |

Media brief:

```text
Prepare responsive real-product media using the supplied front, side, and hinge images. Preserve the exact SKU. Keep critical copy, price, variants, and CTA as semantic HTML. Provide concise alt text describing only visible facts; do not place a fake Add to Cart button inside an image.
```

Events to implement after theme confirmation: variant_select, gallery_interaction, faq_open, add_to_cart, begin_checkout.

## QA result

Pass: the skill produced a responsive content system instead of fixed screens and correctly blocked missing commerce, policy, and specification fields.

