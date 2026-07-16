---
name: sku-reference-migration
description: "Analyze user-provided or authorized reference product-detail pages, long screenshots, page slices, or competitor examples; semantically segment modules, abstract layout/camera/light/material/graphic/narrative language, create REFERENCE_MIGRATION_CONTEXT and M1/M2/M3 migration mappings, and hand an approved target blueprint to marketplace Skills while protecting real SKU facts and reference rights. Use when users mention 参考详情页、迁移详情页、照这个页面做、复刻结构、借鉴风格、竞品长图、参考页面拆解、把参考页换成我的商品、同款排版、相似详情页 or cross-platform page adaptation."
---

# 参考详情页迁移

把用户提供的参考详情页从“可观看的长图”转换成“可审计、可批准、可跨平台重排的模块蓝图”。迁移抽象方法和叙事逻辑，不把参考商品、品牌资产或未经证实的卖点带进真实 SKU。

## 读取规则

开始时完整读取 [`references/reference-migration-system.md`](references/reference-migration-system.md)。需要建立或补全真实商品事实时使用 `$sku-product-core`；目标平台确认后读取命中平台 Skill 的槽位与规划规则完成映射，用户批准方向后才把它作为正式生产接手方并加载逐单元生产协议。

## 工作流

1. 接收参考长图、页面截图、切片、URL 截图或用户已有页面，同时识别真实 SKU 产品图、`SKU_CONTEXT`、目标平台和当前阶段。
2. 没有 `SKU_CONTEXT` 或 `IDENTITY_CONTRACT` 时，先在同一任务中使用 `$sku-product-core`。只有参考页、没有真实产品资料时，只能输出参考分析，不能输出可发布生产 Prompt。
3. 记录参考来源、权利状态和用途。用户自有或明确授权素材可考虑 M2；竞品、来源不明或仅供研究的素材默认使用 M1 或 M3。M1/M2/M3 是内部迁移风险控制，不是对版权、商标、肖像或不正当竞争问题的法律结论。
4. 按语义而非固定像素高度分段，为每个模块记录商业任务、信息类型、构图、镜头、光线、材质、图形系统、叙事位置和不可迁移元素。
5. 创建或合并顶层 `REFERENCE_MIGRATION_CONTEXT`，不要另建第二份权威状态。即使只有一个目标平台，也建立一个稳定的 `platform_contexts[].context_id`；每个目标平台在 `platform_migrations` 中拥有独立迁移条目并通过该 ID 关联。
6. 为每个参考模块建立 `keep / adapt / replace / discard` 映射，绑定真实 SKU 证据、目标平台槽位、F0–F3、允许迁移的抽象特征和明确排除的参考元素。
7. 根据权利边界、目标差异与创意目标选择 M1、M2 或 M3。平台规则始终覆盖参考页比例、模块数量、文字覆盖、主图背景和发布限制。
8. 提出三个差异化迁移方向；任意两个方向至少在创意命题、场景世界、商品角色、镜头与光线、图形系统、叙事节奏中的三个维度不同。多平台默认共用一个创意母方向、分别重排；若平台任务本质不同，允许在一次结构化决策中为各平台分别选择方向，并保存独立批准状态。
9. 用户确认迁移方向前，不输出正式逐单元 Prompt，不进入生成，不写最终交付目录。用户说“按你推荐的来”可视为确认，但要记录所选方向和默认假设。
10. 确认后把所选迁移方向同步到当前平台的 `creative_context_overrides` 与 `direction_state`，再把批准的模块映射交给目标平台 Skill；不要并行维护第二套相互冲突的创意方向。继续策划—提示词—生成分离和逐单元生产，断点恢复时复用已有分段、映射、拒绝方向与批准状态。

## 迁移模式

- `M1｜结构迁移`：复用信息顺序、模块职责和节奏，不复用具体视觉表达。适合竞品研究和跨平台重排。
- `M2｜视觉语言迁移`：复用经过授权的构图、镜头、光线、材质和图形语法，同时替换为真实 SKU 证据。仅用于用户自有、品牌自有或明确授权素材。
- `M3｜创意再诠释`：只保留参考页的问题解决方式和情绪目标，重新导演视觉世界与叙事。来源不明或希望明显拉开差异时默认推荐。

## 硬边界

- 参考页中的商品、Logo、商标、包装、人物、文案、参数、价格、认证、评价和品牌故事不是目标 SKU 的证据。
- 不逐像素复刻竞品页面，不输出会造成来源混淆的独特版式、符号组合或识别性视觉资产。
- 不把整张超长参考页直接塞进生成模型作为最终控制图；先分段、抽象、映射，再按目标槽位生产。
- 真实商品身份由 `IDENTITY_CONTRACT` 和 F0–F3 控制；参考页不能授权改变颜色、结构、比例、Logo、包装文字或隐藏结构。
- 目标平台规则高于参考页规则。无法确认当前规则时标记 `human-review`，不要假定参考页做法可以发布。

## 输出

默认输出：`参考来源与权利状态`、`语义模块地图`、`参考视觉 Token`、`不可迁移元素`、`M1/M2/M3 选择`、`目标模块映射`、`三个差异化迁移方向`、`推荐理由`、`等待确认的唯一决策`。用户确认后再输出平台化资产地图和逐单元生产记录。
