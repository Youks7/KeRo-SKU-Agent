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

目标平台：暂未确定，请根据销售场景推荐；“抖音商城”不要当成 TikTok Shop
输出语言：中文
预计素材：由目标平台的真实槽位决定，不预设固定屏数
核心卖点：暂不确定，请根据图片谨慎判断

请在同一任务中完成产品事实分析、平台识别和方向提案。
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
选择你推荐的产品识别与结构证据方向，产品处理使用模式 A。
画面克制，不要用“高级”替代具体产品证据。
```

## Stage 3 Requirement

```text
按目标平台的真实素材槽位逐单元输出，不预设 8 屏或统一 9:16。
产品本体必须保持真实结构、镜片颜色、镜框比例、Logo 和关键细节一致。
模式 A 的生成 Prompt 只生成背景层，不描述或重绘产品本体；产品专属细节放在真实图合成与质检字段。
最终文字和参数后期排版，不要让图像模型生成最终文字。
```

## QA Checklist

- Lens color did not change.
- Frame shape did not change.
- Hinge and bridge structure are preserved.
- Logo and package text are not invented.
- No unverified UV, polarized, or safety claims.
- Each screen has a distinct sales task and composition.
