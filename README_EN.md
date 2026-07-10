<h1 align="center">Protect the real SKU first. Then build product pages that do not look templated.</h1>

<p align="center"><strong>KeRo SKU Skill</strong></p>

<p align="center">Real-product fidelity · Three-stage decisions · Differentiated production · Screen-by-screen visuals</p>

<p align="center">The uploaded product is the only source of product identity. Formal generation starts only after the direction is approved.</p>

<p align="center">
  <a href="./README.md">简体中文</a> ·
  English ·
  <a href="./README_ZH-TW.md">繁體中文</a><br>
  <a href="./SKU详情页导演Skill/SKU详情页导演Skill.skill">Download Skill</a> ·
  <a href="./SKU详情页导演Skill/sku-detail-page-director/references/SKU详情页导演Skill_Lite_V1.2.1_防同质化生产优化版.md">Full rules (Simplified Chinese)</a> ·
  <a href="https://x.com/Isonlyonenice">X: @Isonlyonenice</a>
</p>

---

## What is this?

KeRo SKU Skill is a Codex skill for e-commerce operators, designers, and AIGC creators.

After you upload real product images, it identifies verifiable facts and fidelity risks, then proposes three clearly different visual directions. It creates per-screen plans and image-generation prompts only after you approve a direction.

It supports Taobao, Tmall, JD.com, Pinduoduo, Douyin Shop, Xiaohongshu, Amazon, Shopify, TikTok Shop, and other e-commerce platforms.

## Build a product page in three stages

| Stage | What AI does | What you do |
| --- | --- | --- |
| 01 Product analysis | Identifies the product, fact boundaries, risks, and visual opportunities | Upload real product images |
| 02 Direction proposal | Provides three distinct A / B / C directions | Select one direction or combine them |
| 03 Visual production | Produces per-screen plans, prompts, and QA requirements | Confirm screen count, aspect ratio, and delivery format |

```text
Real product images
        ↓
Deep product analysis
        ↓
Choose direction A / B / C
        ↓
Per-screen plan and commercial visuals
```

## Quick start

### 1. Install

Download [`SKU详情页导演Skill.skill`](./SKU详情页导演Skill/SKU详情页导演Skill.skill) and import it into Codex.

Alternatively, copy the complete `SKU详情页导演Skill/sku-detail-page-director/` directory into your Codex skills directory.

### 2. Upload product images

Provide front, side, 45-degree, detail, and packaging images whenever possible. Photograph critical logos, structures, lenses, ports, and package text separately.

### 3. Send the starter prompt

```text
Use $sku-detail-page-director to analyze the uploaded product images.

Start with Stage 1: deep product analysis.
Do not produce formal image-generation prompts until I approve a direction.
Do not invent specifications, materials, certifications, claims, or reviews that cannot be verified from the images or supplied documents.
```

## Standard workflow

### Stage 1: Deep product analysis

```text
These are my product images. Complete Stage 1: deep product analysis.

Target platform: Amazon
Output language: English
Expected deliverable: 5–7 listing images or 5–6 A+ modules
Core selling points: not confirmed yet; infer cautiously from visible evidence

Do not invent unverified specifications, materials, certifications, claims, functions, or customer reviews.
```

Stage 1 covers:

- Verified facts and prohibited claims
- Recommended product-handling mode and its risks
- Product character, sales opportunities, and category-template scan
- Three product-specific visual memory points
- The single decision required for the next step

### Stage 2: Select a direction

```text
Continue to Stage 2 and propose three product-page directions.
```

Reply with one direction:

```text
Choose A.
```

Or combine directions:

```text
Combine A and C. Use A's conversion structure with C's premium visual language.
```

### Stage 3: Produce each screen

```text
Create eight screens based on the approved direction.
Deliver each screen separately in a 9:16 aspect ratio.
Before generating each image, provide its sales objective, composition, prompt, and product-consistency checks.
```

For production work, add final text, logos, specifications, and CTAs in post-production. AI-generated text can be used for previews, but it must be manually proofread.

## Product-handling modes

| Mode | Best for | How the product is handled |
| --- | --- | --- |
| A — Strict fidelity | Branded products, premium items, appearance-critical SKUs | Composite the real product cutout; AI generates only backgrounds and lighting |
| B — AI-assisted product image | Standard SKUs and rapid launches | Edit or lightly redraw from real product images, followed by consistency QA |
| C — Concept generation | New-product proposals and direction tests | Concept exploration only; never present it as a real SKU image |

## Non-negotiable rules

1. Real product images are the only source of product identity.
2. Competitor images may guide composition, rhythm, and information structure, but never product design, logos, copy, or brand assets.
3. Never invent a brand, specification, dimension, material, certification, claim, review, or after-sales promise.
4. If the material is unverified, describe only a visible finish or visual impression.
5. Do not alter the SKU's color, structure, proportions, logo, or distinctive details.
6. Every screen needs a different sales objective, composition, and product-specific visual memory point.

---

## Advanced SOP

The following sections are collapsed by default. Open only what you need.

<details>
<summary><strong>Complete input checklist</strong></summary>

You do not need to complete this list at once. Start with product images and known facts, then add missing details during the workflow.

1. Product name
2. Target platform
3. Required deliverables: detail page, hero image, SKU image, secondary image, or A+ module
4. Image size or aspect ratio
5. Front, side, 45-degree, detail, packaging, SKU, and in-use images
6. Primary SKU
7. All colors, styles, specifications, and bundles
8. The three most important selling points
9. Dimensions, weight, material, specifications, colors, and package contents
10. Test reports, certifications, patents, authorization, or quality reports
11. Target audience
12. Primary use scenarios
13. Preferred visual style
14. Reference images or competitor links
15. Prohibited claims or visual elements
16. Logo, brand colors, fonts, and packaging source files
17. Delivery deadline

</details>

<details>
<summary><strong>Correcting analysis errors</strong></summary>

Do not restart the entire project. Correct only the inaccurate information.

```text
Correction:
The target platforms are now Xiaohongshu and Douyin Shop.
The primary selling points are portability and visual appeal; this is not positioned as a low-price product.
The material is unverified and must not be stated as fact.
Revise Stage 1 with these facts, then propose three directions.
```

If the product category was identified incorrectly:

```text
Correction: this is not a kitchen product. It is a pet water dispenser.
The material and capacity are currently unverified.
Redo Stage 1 using this corrected category.
```

</details>

<details>
<summary><strong>Using competitor pages safely</strong></summary>

```text
I uploaded real product images and competitor reference pages.

My product images are the source of truth for product identity.
Use the competitor pages only for visual language, composition rhythm, and information structure.
Do not copy the competitor's product, logo, text, or brand assets.

Complete Stage 1 before proposing directions.
```

To add your own theme:

```text
Use the competitor page only as a structural reference.
Build my page around fishing as the primary use scenario with a restrained, minimal visual language.
Keep the real product fully consistent.
```

</details>

<details>
<summary><strong>Competitor prompt extraction and product migration</strong></summary>

First, extract the reference structure:

```text
Analyze the ten competitor product-page images I uploaded.
For each image, extract the sales objective, composition, scene, lighting, props, text-safe area, and visual rhythm.
Produce ten matching background or scene prompts.

Do not copy the competitor's product, logo, text, or brand assets.
```

Then upload your real product:

```text
The newly uploaded images show my real product and are the only source of product identity.
Apply the extracted structures while preserving the exact product color, geometry, proportions, logo, and distinctive details.
Run a product-consistency check before generating every image.
```

For Amazon:

```text
Create Amazon listing images or A+ module assets from the approved prompts.
Choose the aspect ratio according to each module's purpose; do not force every image into 9:16.
```

</details>

<details>
<summary><strong>Domestic e-commerce and Amazon SKU drafts</strong></summary>

Domestic e-commerce:

```text
Create a draft SKU information sheet from the uploaded multi-angle product images.
Complete Stage 1 only. Do not create directions, screen plans, or image prompts yet.

Output: product name, audience, selling points, visible material finish, usage, and Chinese category path.
Do not invent facts that cannot be verified.
```

Amazon:

```text
Create a draft SKU information sheet from the uploaded multi-angle product images.
Complete Stage 1 only. Do not create directions, module plans, or image prompts yet.

Output: Product Name, Target Audience, Selling Points, Visible Material or Finish, Usage, and Amazon Category Path.
Do not invent unverified material, dimensions, weight, certification, functions, package contents, brand, or model information.
```

</details>

<details>
<summary><strong>Common image-editing prompts</strong></summary>

#### 1:1 hero-image product replacement

```text
Keep Image 1's scene, composition, lighting, and negative space unchanged.
Replace its product with the real products shown in Images 2–11.
Preserve each SKU's exact color, structure, logo, and proportions. Output separate 1:1 hero images.
```

#### White-background product image

```text
Convert these product images into clean commercial studio shots on pure white.
Preserve the real geometry and colors. Remove distracting reflections while keeping controlled highlights and contact shadows that communicate real material and optical depth.
```

#### Change lens color

```text
Change only the lens color in Image 1 to match Image 2.
Do not alter the frame, temples, logo, structure, or proportions.
Keep realistic optical depth; the lenses must not become flat color fills or glowing plastic.
```

#### Five-view layout

```text
Use Image 1 as the five-view layout template.
Use the real product images in Images 2–11 to create front, side, 45-degree, rear, and detail views.
Do not invent hidden geometry for missing angles; mark missing views explicitly.
```

#### Premium sunglasses rendering

```text
Use the uploaded sunglasses as the strict product reference.
Preserve the exact frame, temples, lenses, bridge, hinges, logo, colors, coating direction, details, and proportions.

Improve only the commercial rendering quality: crisp industrial edges, controlled satin highlights, realistic optical lens depth, clean reflections, a white-to-light-gray studio background, and a soft natural contact shadow.

Do not redesign, reshape, recolor, replace, or stylize the product.
```

</details>

<details>
<summary><strong>Final commercial QA checklist</strong></summary>

1. Does the product color match the real images?
2. Did the structure, proportions, or SKU change?
3. Are logos, packaging text, and distinctive details accurate?
4. Were nonexistent accessories, certifications, claims, or functions added?
5. Was a competitor or look-alike product substituted for the real product?
6. Do lenses, reflections, and materials look physically believable?
7. Does every screen have a unique sales objective and composition?
8. Does every prompt contain product-specific details?
9. Was all final text manually proofread and typeset?
10. Is the image ready for commercial use, or only suitable as a direction reference?

</details>

## Repository structure

```text
SKU详情页导演Skill/
├── sku-detail-page-director/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/
│       └── SKU详情页导演Skill_Lite_V1.2.1_防同质化生产优化版.md
└── SKU详情页导演Skill.skill
```

Current version: **Lite V1.2.1 — Differentiated Production Edition**

---

## About me

**Qiushui Kero** — an AIGC creator who enjoys experimenting with new tools and sharing unusual, practical AI workflows.

X: [@Isonlyonenice](https://x.com/Isonlyonenice)
