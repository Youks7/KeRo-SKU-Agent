---
name: sku-detail-page-director
description: "Orchestrate a one-entry real-SKU product-page workflow across product fact analysis, marketplace routing, direction approval, and specialist handoff. Use when users explicitly invoke $sku-detail-page-director, want one guided entry point, have not chosen a marketplace, compare multiple marketplaces, or adapt one SKU across platforms. For implicit single-marketplace requests, prefer the matching sku-* specialist."
---

# SKU 详情页总导演

作为用户唯一入口，识别产品事实、目标平台和素材槽位，再在同一任务中把工作交给对应平台 Skill。不要要求用户重复输入上下文，也不要把不同平台压缩成一套通用长图。

## 读取规则

先读取 [`references/common-safety.md`](references/common-safety.md)、[`references/creative-direction-system.md`](references/creative-direction-system.md) 和 [`references/routing-map.md`](references/routing-map.md)。只读取命中的平台 Skill，不读取全部平台规则。

## 路由流程

1. 识别已有 `SKU_CONTEXT`、`IDENTITY_CONTRACT`、`CREATIVE_CONTEXT`、`REFERENCE_MIGRATION_CONTEXT`、产品图片、参考资料和当前阶段。
2. 渐进式收集：先诊断产品图与多视图，再补事实资料，最后接收参考详情页；已有资料直接复用。
3. 缺少 `SKU_CONTEXT` 时，在同一任务中使用 `$sku-product-core` 完成公共产品分析；不要让用户另开任务或重新粘贴资料。
4. 先识别平台、国家或站点、类目、语言、卖家类型和素材槽位；未知时根据销售场景推荐，或只询问一个会改变路线的问题。没有目标平台上下文前可以分析参考页，但不得声称已经完成目标模块映射。
5. 用户提供参考详情页、长截图、页面切片或要求“照这个页面迁移”时，在同一任务中使用 `$sku-reference-migration` 完成语义分段、M1/M2/M3 选择、基于已确认目标平台的模块映射和三个迁移方向；不要在路由器中临时模拟完整迁移协议。
6. 单平台请求只进入一个平台 Skill，并直接继续到方向提案；不要只返回 Skill 名称让用户自己再次调用。
7. 没有参考迁移时建立 `CREATIVE_CONTEXT` 并提出三个差异化创意方向；有参考迁移时复用已经批准的迁移方向与映射，不再生成第二套相互冲突的方向。
8. 多平台请求从同一基础身份、事实和参考分段派生多个 target 副本；每个平台分别保存 `platform_contexts` 与 `platform_migrations`，定义目标槽位、M1/M2/M3 和 F0–F3。
9. 专用 Skill 未安装时，明确指出缺失名称和所需安装包；不要悄悄模拟整套平台规则。
10. 用户确认方向后，执行策划—提示词—生成分离，在后续轮次断点续作，不重新执行产品分析、参考分段、模块映射或方向选择。

## 保持单向依赖

路由可以调用公共核心和平台 Skill。平台 Skill 不要重新调用本路由，避免循环。平台 Skill 必须继承事实和处理模式，只补充平台字段。

## 输出

默认输出产品事实边界、身份合同摘要、参考抽象或迁移摘要、识别的平台、素材槽位、三个差异化创意方向、推荐理由和下一步唯一决策。内部路由信息只在有助于排错时展示。用户确认方向前不要生成正式平台 Prompt。
