---
name: sku-product-core
description: "Analyze real product images and supplied documents to establish verified SKU identity, evidence boundaries, an IDENTITY_CONTRACT, multi-view confidence, product-specific visual memory points, and a reusable SKU_CONTEXT V2. Use before platform production when facts are not normalized, when multiple marketplaces share one product, or when users ask for 产品事实分析、身份锁定、商品图保真、F0–F3、禁止编造、参考安全抽象或跨平台 SKU 上下文。"
---

# SKU 产品事实核心

把真实产品资料整理为所有平台可复用的事实与保真上下文。只完成公共产品分析，不生成平台尺寸、页面结构或正式生图 Prompt。

## 读取规则

完整读取：

- [`references/core-rules.md`](references/core-rules.md)
- [`references/sku-context-schema.md`](references/sku-context-schema.md)
- [`references/core-qa.md`](references/core-qa.md)

只有用户要求竞品扫描、类目同质化判断或参考竞品时，再读取 [`references/competitor-research.md`](references/competitor-research.md)。没有实际检索或用户提供的竞品素材时，只能称为经验性启发。

## 工作流

1. 盘点产品图、包装图、规格表、认证、品牌资产和用户陈述。
2. 分开记录已确认事实、谨慎推断、禁止主张和缺失证据。
3. 诊断每张产品图的质量、角色与视角，统一同一 SKU 的多视图并记录 `view_confidence`。
4. 建立 `IDENTITY_CONTRACT`，分开不可变、有限可变、未知特征及允许/禁止变换。
5. 提炼三个有图片或资料证据的产品专属视觉记忆点。
6. 为每个候选平台槽位建议 F0–F3，不用全局模式锁死全部素材。
7. 标记高风险类目和需要人工或法律复核的主张。
8. 按标准结构输出 `SKU_CONTEXT V2`，供后续建立 `CREATIVE_CONTEXT`。
9. 每轮只提出真正会改变真实性或平台路线的问题，其他未知项保持为空。

## 边界

不要选择平台方向，不要输出固定屏数，不要生成价格、参数、认证或正式广告承诺。用户指定平台时，把完成的 `SKU_CONTEXT` 交给对应平台 Skill。
