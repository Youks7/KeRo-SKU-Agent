# Troubleshooting

## Skill Does Not Trigger

Use the exact platform Skill name:

```text
$sku-amazon
$sku-1688
$sku-shopify
```

Use `$sku-detail-page-director` when the platform is unknown or several platforms are requested. Confirm that the selected `.skill` package is installed.

Also check that the installed folder contains:

```text
SKILL.md
references/
agents/
```

## Platform Skill Repeats Product Analysis

Generate one shared context first:

```text
请使用 $sku-product-core 生成 SKU_CONTEXT。
平台 Skill 必须继承其中的已确认事实、禁止主张和产品处理模式，不要重新开始。
```

## Product Shape Changes In Generated Images

Switch to strict fidelity mode:

```text
这个 SKU 外观必须严格一致。
请使用模式 A：严格保真。
产品本体使用真实产品抠图，AI 只生成背景、光影、场景和留白。
```

## Product Material Was Invented

Correct the fact boundary:

```text
材质不能确认，不要写成事实。
只能描述为“可见质感”或“视觉上接近”。
请修正阶段一，并继续给我 3 个方向。
```

## AI Text Looks Wrong

Use generated text only for preview. For final commercial use, add:

```text
最终标题、卖点、参数、Logo、认证标识和 CTA 都由后期排版完成。
生图 Prompt 中不要让图像模型生成最终文字。
```

## Competitor Reference Feels Too Similar

Use this correction:

```text
竞品图只参考构图节奏和信息结构。
不要复制竞品产品、Logo、文字、包装、配色和品牌资产。
请重写方向，让首屏构图、背景材质和视觉记忆点明显不同。
```

## Platform Output Looks Like a Generic Long Page

Invoke the dedicated skill and name the asset slot:

```text
$sku-taobao：淘宝主图、轮播图、SKU属性图或详情模块
$sku-amazon：Main Image、secondary images或A+ module
$sku-shopify：PDP sections、variant media和真实CTA组件
$sku-tiktok-shop：PDP main image、additional images或内容交接
```

Do not ask for one universal ratio across unrelated asset slots.

## Chinese Path Issues

If a tool cannot read:

```text
SKU详情页导演Skill/
```

copy the inner folder instead:

```text
sku-detail-page-director/
```
