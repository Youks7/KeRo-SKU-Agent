# Forward Run: sku-jd

## Input preservation

Use the supplied `SKU_CONTEXT`, mode A. Model, dimensions, package list, compatibility, warranty, and performance evidence are missing.

## Direction proposal

- A — Structure and parameter certainty: visible construction first, verified parameter table later.
- B — Fit and use guidance: only after dimensions and intended-user information are supplied.
- C — Service confidence: only after warranty entity and terms are supplied.

Recommended: A. It can proceed using visible construction while keeping unknown fields blocked.

## Parameter—evidence matrix

| Field | Value | Evidence | State |
| --- | --- | --- | --- |
| Frame color | black | front.jpg | verified |
| Lens color | dark | front.jpg | verified |
| Dimensions | unknown | none | blocked |
| Lens performance | unknown | none | blocked |
| Warranty | unknown | none | blocked |

## Confirmed production

Modules: real-product main media, angle overview, hinge detail, editable parameter table, package list, fit/usage conditions, and service terms. Only the first three are currently producible.

Representative prompt:

```text
Generate only a precise neutral product-photography background with soft controlled lighting and a reserved area for the real black sunglasses cutout, secondary close-up zone for the verified hinge crop, no product, no performance diagram, no technical numbers, no certificate, no text, no logo.
```

## QA result

Pass with correct evidence gating: visual structure is usable; parameters, compatibility, package contents, and service claims remain blocked.

