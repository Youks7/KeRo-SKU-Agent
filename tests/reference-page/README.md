# Synthetic reference-page visual fixture

`synthetic-competitor-long-page.png` is a self-created 1000 × 4000 px fictional sunglasses product page used to forward-test actual long-image inspection and semantic segmentation without committing third-party product or brand assets.

- SHA-256: `AFB03900B8B930EA0588740355B615770A35804B0D81EDA90F57E4515164F2F0`
- Source: `synthetic-competitor-long-page.svg`
- Rights: repository-owned synthetic test fixture
- Test role: treated as `competitor-analysis` so the Skill must still exclude its fictional product, brand, copy, claims, price, reviews, CTA, and visual identity.

The SVG source is committed so the fixture is auditable and reproducible. The expected semantic segmentation is intentionally not embedded in this directory; the independent visual forward test must inspect the PNG pixels before producing its module map. This fixture tests visual intake and workflow behavior, not actual model-generated commercial output.
