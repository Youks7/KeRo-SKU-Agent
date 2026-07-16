# V1.4 Cross-Platform Sunglasses Example

This regression example demonstrates identity-locked creative reconstruction. It contains no commercial performance claims.

## Product category and target platforms

- Category: real sunglasses SKU.
- Targets: Taobao/Tmall/JD/Pinduoduo/1688/Amazon/Shopify/TikTok Shop, with independent asset maps.

## Required input material

- Front, side, three-quarter, hinge, Logo, packaging, and variant images when available.
- Verified specification and included-item records.
- Optional reference detail page or style images with their roles and rights status.

## Starter prompt

```text
请使用 $sku-detail-page-director 渐进分析这副真实墨镜。
先诊断产品图、统一多视图并建立 SKU_CONTEXT V2 与 IDENTITY_CONTRACT；
再对我提供的参考详情页做语义分段和参考抽象，按目标平台槽位建立 CREATIVE_CONTEXT。
请提出三个差异化方向，不要每屏重复同一张原图抠图。
不得编造偏光、UV、防蓝光、材质、尺寸、认证或包含物。
方向确认前不要输出正式生产 Prompt。
```

## Stage 1 expected output

- Image-quality diagnosis and a source-role map.
- Multi-view consistency result and `view_confidence` for front, side, hinge, and hidden geometry.
- Verified, inferred, prohibited, and missing facts.
- The identity contract below and three evidence-backed visual memory points.
- Platform/slot questions that materially change F0–F3 routing.

## Shared identity

Use `front.jpg`, `side.jpg`, and `hinge.jpg` as the evidence board. Lock the lens outline, bridge, hinge, temple starting point, Logo position, frame proportions, and lens tint. Keep hidden geometry and material unknown.

Do not claim polarization, UV protection, blue-light filtering, material, certification, dimensions, or included items without supporting evidence.

## Three creative directions

1. Optical Sculpture: translucent acrylic, geometric plinths, hard contour light, hero three-quarter view, and hinge macro.
2. Urban Mirror: real city glass and stone, wearing movement, natural hard daylight, environmental reflection, and editorial grids.
3. Travel Daylight: warm stone, window light, hand-held and storage moments, golden-hour side light, and a relaxed narrative.

These directions must differ in thesis, visual world, product role, camera/light, and narrative arc. A background-color change does not count.

## Stage 2 direction-selection example

```text
确认 Urban Mirror / 城市镜面方向。
Amazon Main 和 TikTok Shop PDP Main 保持 F0；
允许的附图、详情和 Shopify 媒体可以使用 F1/F2。
请保存 CREATIVE_CONTEXT 和选择结果，从平台资产地图继续。
```

## Slot routing

- Amazon Main Image and TikTok Shop PDP Main Image: F0.
- Taobao/Tmall/JD/Pinduoduo controlled detail assets: F1 or reviewed F2 when the current slot allows it.
- Amazon Secondary/A+, Shopify Gallery/Hero, approved marketplace detail scenes: F1/F2.
- 1688 product, packaging, MOQ, price, QC, and delivery evidence: F0 or real data components; atmosphere cannot replace procurement proof.
- F3 stays direction-only on every platform.

## F2 gate

An F2 wearing or new-camera asset remains `human-review` until a person compares all identity landmarks against the three source views. If geometry, Logo, or lens tint drifts, repair it or fall back to F1/F0.

## Stage 3 per-unit production example

```text
生产单元：Shopify Gallery / 淘宝允许场景化的详情模块
创意命题：镜框几何与城市建筑线条形成穿搭呼应。
产品处理模式：F2
来源：front.jpg + side.jpg + hinge.jpg
身份锚点：镜片外轮廓、鼻梁、铰链、镜腿起点、Logo 位置、镜片色调
允许：真实人物、城市玻璃与石材、自然硬日光、有侧面证据支持的新机位
禁止：发明隐藏结构、改变镜片色调、移动 Logo、加入未验证功能图形
发布闸门：输出保持 human-review；逐项比对三张来源图后才可发布
```

The complete unit must also include the platform slot, sales task, creative-freedom score, reference abstraction, copy-safe area, shot matrix, Prompt, Negative Prompt, post-production layout, identity QA, and generic-prompt interception required by `shared/per-unit-production.md`.

## Product-fidelity and creative-quality QA checklist

- The frame silhouette, bridge, hinge, temple start, Logo position, proportions, and lens tint match the identity contract.
- New views do not reveal unsupported hidden geometry.
- Main/SKU/variation evidence slots do not use an impermissible reconstruction mode.
- The three directions differ in at least three creative dimensions and are not color swaps.
- Scene, reflection, model, props, and scale do not imply an unverified feature or included item.
- Reference traits are abstracted; competitor product, person identity, Logo, copy, and unique campaign symbols are excluded.
- Final text, Logo, price, parameters, certification, and CTA use real layers or HTML.
- F2 remains `human-review`; identity failure becomes `repair-required` or falls back to F1/F0.
