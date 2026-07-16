# Troubleshooting

## Skill Does Not Trigger

Use the exact platform Skill name:

```text
$sku-amazon
$sku-1688
$sku-shopify
$sku-reference-migration
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
请检查 IDENTITY_CONTRACT 和当前素材槽位。
主图、SKU 图或证据槽位使用 F0；允许场景化但模型身份不稳定时使用 F1。
只有多视图、身份锚点、平台许可和人工审核都具备时才使用 F2。
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
请使用 $sku-reference-migration，把来源标记为 competitor-analysis。
只允许 M1 结构迁移或 M3 创意再诠释，不允许 M2。
排除竞品产品、人物、Logo、文字、包装、专属配色组合和独特品牌资产。
请重写三个迁移方向，并确保任意两个方向至少有三个创意维度不同。
```

## Reference Page Was Copied Into The Wrong Platform Shape

```text
不要继承参考页的平台比例、模块数量、长图长度或叠字方式。
请先把参考模块还原为购买问题，再建立目标平台的 module_mapping。
目标平台规则必须写入 platform_override；每个非 discard 单元绑定真实 SKU 证据。
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
