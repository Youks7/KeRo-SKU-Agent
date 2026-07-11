# Example: Sunglasses Detail Page

## Scenario

You have real sunglasses product images and want to create a high-conversion e-commerce detail page without changing the frame, lens, color, or logo.

## Input Material

Recommended:

- Front view
- Side view
- 45-degree view
- Lens close-up
- Hinge close-up
- Packaging image

## Starter Prompt

```text
请使用 $sku-detail-page-director 分析我上传的墨镜产品图。

目标平台：淘宝 / 抖音商城通用
输出语言：中文
预计屏数：8 屏
核心卖点：暂不确定，请根据图片谨慎判断

先执行阶段一：产品深度分析。
在我确认方向前，不要输出正式生图 Prompt。
不能编造材质、UV 防护、偏光、认证、品牌故事或用户评价。
```

## Stage 1 Should Clarify

- The visible frame shape, lens color, bridge, hinge, and packaging details.
- Which details must remain unchanged.
- Whether strict fidelity mode is needed.
- Which claims cannot be used without documents.
- Visual memory points from the product itself.

## Direction Selection

Example reply:

```text
选 C，但保留 A 的严格保真方式。
画面要高级，不要低价促销感。
```

## Stage 3 Requirement

```text
按确认方向制作 8 屏。
每一屏单独输出，比例 9:16。
产品本体必须保持真实结构、镜片颜色、镜框比例、Logo 和关键细节一致。
最终文字和参数后期排版，不要让图像模型生成最终文字。
```

## QA Checklist

- Lens color did not change.
- Frame shape did not change.
- Hinge and bridge structure are preserved.
- Logo and package text are not invented.
- No unverified UV, polarized, or safety claims.
- Each screen has a distinct sales task and composition.
