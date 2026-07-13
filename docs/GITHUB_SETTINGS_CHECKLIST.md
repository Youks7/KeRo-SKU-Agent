# GitHub Settings Checklist

These items need to be configured manually in the GitHub repository settings.

## About Section

Recommended description:

```text
Codex Skill for SKU-safe e-commerce detail page planning and product-image prompt workflows.
```

Recommended topics:

```text
codex-skill
ecommerce
sku
product-images
ai-prompts
aigc
amazon
shopify
tiktok-shop
taobao
product-page
```

## Social Preview

Upload:

```text
assets/social-preview.png
```

GitHub path:

```text
Repository Settings -> General -> Social preview
```

## Releases

Create a release only after clean-session model tests and real-product golden fixtures are complete:

```text
v1.3.0
```

Attach:

```text
packages/kero-sku-skills-v1.3-bundle.zip
packages/SHA256SUMS.txt
packages/sku-product-core.skill
packages/sku-detail-page-director.skill
packages/sku-taobao.skill
packages/sku-tmall.skill
packages/sku-pinduoduo.skill
packages/sku-jd.skill
packages/sku-1688.skill
packages/sku-amazon.skill
packages/sku-shopify.skill
packages/sku-tiktok-shop.skill
```

## Repository Features

Recommended:

- Enable Issues.
- Keep Pull Requests enabled.
- Add the social preview image.
- Add repository topics.
- Add a short repository description.

Optional:

- Enable Discussions after there are users asking questions.
- Enable GitHub Pages if the `website/` directory will be deployed.
