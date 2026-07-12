# V1.3 Cross-Platform Example: Sunglasses

This is a fictional regression fixture for workflow testing. It is not a commercial claim set.

## Shared Input

Assume the user supplies front, side, 45-degree, hinge, lens, packaging, and variant images plus a signed specification sheet. The core workflow must derive one shared `SKU_CONTEXT` before platform production.

```yaml
sku_context_version: 1
product_identity:
  category: sunglasses
  source_images:
    - front.jpg
    - side.jpg
    - hinge.jpg
    - package.jpg
  visible_structure:
    - full-rim frame
    - two visible hinges
  primary_colors:
    - black frame
  included_items:
    - pending verification from packaging list
facts:
  verified:
    - The submitted SKU has a black full-rim frame.
  cautious_inferences:
    - The visible surface appears glossy.
  prohibited_claims:
    - UV protection without a report
    - polarization without a report
  missing_evidence:
    - included-item list
    - lens performance report
production:
  handling_mode: A
  prohibited_edits:
    - frame geometry
    - lens color
    - hinge structure
    - logo and packaging text
visual_memory_points:
  - point: frame-to-temple transition visible in the side image
    product_evidence: side.jpg
    suitable_uses: [detail image, product close-up]
```

## Expected Platform Differences

### Taobao

Produce separate main-media, carousel, SKU-property-image, and mobile-detail-module plans. Do not force every asset into 9:16. Keep variant colors mapped to the correct source images.

### Tmall

Add brand-rights and qualification checks, define fixed brand-system elements, and default to strict fidelity for main and packaging assets.

### Pinduoduo

Create a SKU-price-image matrix before visual direction. Block publication if the lowest-price SKU is an accessory while the exposure image shows a full set.

### JD

Create parameter, compatibility, package-content, and warranty evidence tables. Do not claim UV protection or polarization without documents.

### 1688

Replace consumer-only storytelling with verified MOQ, tier pricing, sampling, customization, production, packaging, logistics, quality-control, and inquiry modules. Unknown factory capabilities remain blank.

### Amazon

Use the real product on a compliant Main Image, then plan secondary images and A+ modules separately. Localize units and claims for the selected marketplace.

### Shopify

Produce responsive PDP sections, variant media, metafields, HTML copy fields, alt text, real Add to Cart components, and analytics events instead of an eight-image long page.

### TikTok Shop

Use a real white-background PDP main image where required, map each variation to its own image, and route Shoppable Photo or video concepts to content briefs rather than using them as PDP main media.

## Failure Regression

The following output must fail review:

```text
Polarized UV400 premium sunglasses with certified eye protection.
```

Reason: the fixture does not contain a polarization or UV report. The corrected output must either omit these claims or request the supporting evidence.

