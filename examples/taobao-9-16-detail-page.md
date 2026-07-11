# Example: Taobao / Douyin 9:16 Detail Page

## Scenario

You need a vertical product detail page for domestic e-commerce platforms.

## Starter Prompt

```text
请使用 $sku-detail-page-director 分析我上传的产品图。

目标平台：淘宝 / 抖音商城通用
输出语言：中文
预计屏数：8 屏
核心卖点：暂不确定，请根据图片谨慎判断

先执行阶段一。
在我确认方向前，不要输出正式生图 Prompt。
不能编造图片中无法确认的规格、材质、认证、功效和用户评价。
```

## Recommended Screen Rhythm

1. First screen: product identity and visual hook.
2. Core selling point.
3. Use scenario.
4. Detail close-up.
5. Pain point or comparison.
6. SKU or variant display.
7. Trust or usage reminder without fake claims.
8. Closing visual and CTA area for post-production layout.

## Direction Reply Example

```text
A + C 混合。
以 A 的转化结构为主，加入 C 的高级质感。
不要做低价促销风。
```

## Stage 3 Prompt

```text
按确认方向制作 8 屏。
每屏比例 9:16。
每一屏先输出销售任务、构图、Prompt、Negative Prompt、文字安全区和产品一致性质检点。
```

## Notes

- Do not let the image model create final text.
- Keep a clean text-safe area for later layout.
- Avoid repeating the same product angle for every screen.
- Use product-specific visual memory points instead of generic "premium" styling.
