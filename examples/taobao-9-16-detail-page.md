# Example: Taobao Mobile Detail Modules

## Scenario

You need Taobao-native main media, carousel, SKU images, and mobile detail modules. The legacy filename remains for link compatibility; the workflow no longer treats Taobao and Douyin as one platform or forces every asset to 9:16.

## Starter Prompt

```text
请使用 $sku-detail-page-director 分析我上传的产品图。

目标平台：淘宝
输出语言：中文
目标素材：主图、轮播、SKU 属性图和移动端详情模块
核心卖点：暂不确定，请根据图片谨慎判断

请在同一任务中完成事实分析和淘宝方向提案，不要让我重复调用其他 Skill。
在我确认方向前，不要加载完整生产协议或输出正式生图 Prompt。
不能编造图片中无法确认的规格、材质、认证、功效和用户评价。
```

## Recommended Module Logic

1. Separate search/main media, carousel, SKU property images, and detail modules.
2. Let every slot solve a different commercial task.
3. Derive the detail-module sequence from verified product evidence and purchase uncertainty.
4. Read the current Taobao backend for ratios, dimensions, count, and text-overlay rules.

## Direction Reply Example

```text
选择你推荐的“搜索识别 + 结构证据”方向。
保持真实产品，不做低价促销风；缺少的规格继续留空。
```

## Stage 3 Prompt

```text
按确认方向和淘宝当前素材槽位生产。
不要把主图、轮播、SKU 图和详情模块都做成 9:16。
每个生产单元完整输出来源证据、销售任务、构图、处理模式、Prompt、Negative Prompt、文案位置、后期排版、镜头矩阵和一致性质检。
```

## Notes

- Do not let the image model create final text.
- Use the current backend ratio and keep a clean text-safe area for later layout.
- Avoid repeating the same product angle for every screen.
- Use product-specific visual memory points instead of generic "premium" styling.
