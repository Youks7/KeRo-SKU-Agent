---
name: sku-detail-page-director
description: "Route ambiguous, legacy, or multi-platform real-SKU product-page requests to the correct KeRo specialist workflow. Use when users ask for 商品详情页、SKU 商品图或跨平台适配但尚未确定平台，明确要求比较多个平台，想把同一 SKU 改编到多个电商平台，或显式调用旧版 $sku-detail-page-director。Do not use for a single confirmed marketplace when its dedicated sku-* skill is available."
---

# SKU 详情页总导演

识别目标平台和素材槽位，复用一次产品事实分析，然后把生产任务交给对应平台 Skill。不要把不同平台压缩成一套通用长图。

## 读取规则

先读取 [`references/common-safety.md`](references/common-safety.md) 和 [`references/routing-map.md`](references/routing-map.md)。只读取命中的平台 Skill，不读取全部平台规则。

## 路由流程

1. 识别用户已有的 `SKU_CONTEXT`、产品图片、已确认事实和处理模式。
2. 识别平台、国家或站点、类目、语言、卖家类型和素材槽位。
3. 平台未知时，根据销售场景推荐平台，或只询问一个会改变路线的问题。
4. 缺少 `SKU_CONTEXT` 时，优先使用 `$sku-product-core` 完成公共产品分析。
5. 单平台请求只进入一个平台 Skill。
6. 多平台请求从同一基础 `SKU_CONTEXT` 派生多个 target 副本，分别进入专用 Skill。
7. 专用 Skill 未安装时，明确指出缺失名称和所需安装包；不要悄悄模拟整套平台规则。

## 保持单向依赖

路由可以调用公共核心和平台 Skill。平台 Skill 不要重新调用本路由，避免循环。平台 Skill 必须继承事实和处理模式，只补充平台字段。

## 输出

路由阶段只输出：识别的平台、素材槽位、使用的产品上下文、将启用的 Skill、缺失信息和下一步唯一决策。不要在路由阶段生成正式平台 Prompt。
