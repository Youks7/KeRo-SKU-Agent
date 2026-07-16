# 参考详情页迁移系统

本协议把参考详情页转换为可审计的语义模块、抽象视觉语言和目标平台映射。参考页提供方法启发，不提供目标 SKU 的商品事实。

## 目录

- [输入与角色](#输入与角色)
- [权利状态](#权利状态)
- [语义分段](#语义分段)
- [参考抽象](#参考抽象)
- [迁移模式](#迁移模式)
- [模块映射](#模块映射)
- [跨平台重排](#跨平台重排)
- [三个迁移方向](#三个迁移方向)
- [确认门与生产交接](#确认门与生产交接)
- [质检与断点续作](#质检与断点续作)

## 输入与角色

先识别每份输入的角色，避免把参考页误当商品证据：

| 输入 | 允许作用 | 不允许作用 |
|---|---|---|
| 真实 SKU 图片与文件 | 建立事实、身份合同、F0–F3 来源 | 被参考商品覆盖 |
| 用户陈述 | 建立待确认或已确认事实 | 自动升级为第三方认证 |
| 参考详情页或长截图 | 分析模块职责、构图、节奏与视觉语法 | 证明目标商品的参数、功效或包含物 |
| 平台规则 | 决定目标槽位、发布限制和合规闸门 | 被参考页做法覆盖 |

只有参考页、没有真实 SKU 素材时，输出可复用的参考分析，但把生产状态设为 `blocked`。不得生成可被误认为目标商品成品的正式 Prompt。

## 权利状态

在 `source.rights_status` 中只使用以下值：

- `self-owned`：用户或其品牌拥有页面及视觉资产。
- `authorized`：用户明确说明已获使用授权。
- `competitor-analysis`：竞品或第三方页面，仅用于研究。
- `unknown`：来源或权利范围不明。

权利状态决定可用模式，但不替代目标 SKU 的事实验证：

- `self-owned` / `authorized`：可选择 M1、M2 或 M3。
- `competitor-analysis` / `unknown`：只使用 M1 或 M3；默认推荐 M3。
- 用户要求逐像素复刻第三方页面时，改为 M1 结构迁移或 M3 创意再诠释，并明确排除识别性元素。

M1/M2/M3 是工作流内部的风险控制和原创距离选择，不构成对版权、商标、肖像、合同或不正当竞争风险的法律结论。权利状态不清或发布风险较高时保留人工审核。

## 语义分段

不要按固定像素高度、固定六屏或视觉色块机械切分。先通览全页，再按一个模块解决的购买问题切分。

每个 `semantic_modules[]` 至少记录：

- `source_module_id`：稳定且可恢复的编号。
- `source_region`：页内范围或切片文件，不要求虚构精确像素。
- `module_role`：识别、利益、证据、规格、使用、信任、消除顾虑或行动。
- `customer_question`：该模块回答的购买问题。
- `information_type`：事实、声明、视觉演示、参数、流程或品牌叙事。
- `composition`、`camera`、`lighting`、`material`、`graphic_system`、`narrative_position`。
- `protected_or_unique_elements`：不得迁移的商品、品牌、人物、文案、符号或独特组合。
- `reusability`：`method-only`、`authorized-visual-language` 或 `discard`。

长页先建立模块清单与缩略总览，再逐模块分析。整张长图不作为最终生成控制图。

## 参考抽象

把可迁移内容抽象为不依赖参考商品本体的 `reference_visual_tokens`：

- 构图语法：产品占比、留白方向、前中后景关系、信息分区。
- 镜头语法：景别序列、机位节奏、细节与全景如何交替。
- 光线语法：主光方向、硬软、反差、轮廓光、反射控制。
- 材质语法：背景触感、表面粗糙度、透明度、层次和环境质感。
- 图形语法：网格、线条、色块、标注、字体层级和信息密度。
- 叙事语法：开场承诺、证据递进、疑虑处理和行动收束。

抽象报告不得包含可直接复刻的竞品产品轮廓、Logo、包装、人物身份、原文案、专属图案、品牌色组合或独特版式坐标。

## 迁移模式

### M1｜结构迁移

保留购买问题的顺序、模块职责和信息节奏，重新设计全部视觉表达。适合竞品研究、跨品类启发和跨平台重排。

### M2｜视觉语言迁移

在 `self-owned` 或 `authorized` 前提下，复用抽象后的构图、镜头、光线、材质、图形和叙事语法。所有商品事实、商品像素、文案和品牌元素仍替换为目标 SKU 的合法来源。

### M3｜创意再诠释

只保留参考页想解决的商业问题和情绪目标，重新提出创意命题、视觉世界和镜头系统。适合第三方参考、来源不明、跨品类或需要明显原创差异的任务。

模式不是保真等级。真实 SKU 仍按每个目标槽位独立选择 F0–F3。

## 模块映射

每个 `module_mapping[]` 必须回答“参考模块如何转成目标平台的真实商品资产”：

```yaml
- source_module_id: REF-03
  target_unit_id: AMZ-SECONDARY-02
  action: adapt                 # keep / adapt / replace / discard
  target_slot: Amazon secondary image
  target_customer_question: null
  target_evidence_ids: []
  handling_mode: F1
  transferable_abstract_features: []
  excluded_reference_elements: []
  platform_override: null
  status: planned              # planned / blocked / approved / produced / repair-required
```

映射规则：

1. `keep` 只表示保留模块商业职责，不表示复制像素。
2. `adapt` 表示抽象方法适配到目标平台和目标证据。
3. `replace` 表示参考模块的任务有价值，但必须用全新结构或更强目标证据替换。
4. `discard` 表示无证据、无目标槽位、违反平台规则或依赖第三方品牌资产。
5. 每个非 `discard` 模块都要绑定 `target_evidence_ids`；缺失时标记 `blocked`。
6. 每个模块单独选择 F0–F3，不从参考页继承商品处理方式。

## 跨平台重排

来源平台只描述参考页当前形态，目标平台决定最终资产地图：

- 不继承来源平台的图片比例、模块数量、长图长度、文字覆盖或 CTA 方式。
- 先把来源模块还原为购买问题，再映射到目标平台合法槽位。
- 一个来源模块可以拆成多个目标单元，多个来源模块也可以合并为一个目标单元。
- Amazon Main Image、SKU / variation 图和其他严格槽位优先使用目标平台规则与 F0。
- Shopify 的价格、Variant、Add to Cart、政策和可访问性内容使用真实组件，不渲染成参考图假按钮。
- 参考迁移任务即使只有一个目标平台，也建立稳定的 `platform_contexts[].context_id`；每个目标在 `platform_migrations` 中保存独立映射并用 `target_platform_context_id` 关联，不覆盖其他平台进度。
- 目标平台天然需要、但不来自任何参考模块的内容写入 `platform_native_units`，例如 Shopify 的真实价格、Variant、Add to Cart、配送政策和 Amazon 的资格性模块；不要伪造一个 `source_module_id` 强行挂靠。

## 三个迁移方向

每个方向卡至少包含：

- 方向名称与 `creative_thesis`。
- 迁移模式和迁移强度。
- `visual_world` 与商品角色。
- 镜头、光线、材质、图形系统和叙事节奏。
- 继承的抽象方法、明确舍弃的参考元素。
- 目标平台适用槽位、推荐 F0–F3 范围和主要风险。

任意两个方向至少在六个维度中的三个不同：创意命题、场景世界、商品角色、镜头与光线、图形系统、叙事节奏。只换背景颜色、道具或“高级感”形容词不算新方向。

多平台任务默认提出三个可跨平台复用的创意母方向，再分别做目标平台映射。用户可以一次批准同一个母方向应用于所有平台，也可以在一次结构化决策中指定 `Amazon=D1，Shopify=D2`；后一种情况必须分别写入每个 `platform_migrations[].selected_direction` 和对应平台批准状态，不能用活动平台覆盖其他平台。

## 确认门与生产交接

在 `approval_status: approved` 前：

- 允许输出参考分析、模块地图、迁移模式、三方向与推荐。
- 不允许输出正式逐单元 Prompt、进入生成或写最终交付目录。
- 只询问一个会改变迁移路线的决定；用户说“按你推荐的来”可记录为批准推荐方向。

确认前可以读取目标平台 Skill 的槽位、资格和规划规则，以便完成合法模块映射；不得因此提前加载正式逐单元生产协议或输出正式 Prompt。批准后，把当前平台迁移条目的 `selected_direction` 同步到对应 `platform_contexts[].creative_context_overrides` 与 `direction_state`；单平台投影视图同时更新当前 `CREATIVE_CONTEXT`。迁移方向成为该平台唯一批准方向，不再并行生成第二套方向。然后把 `module_mapping`、`platform_native_units`、`reference_visual_tokens`、`excluded_elements` 和 `qa` 交给目标平台 Skill，重新核对目标槽位和平台规则，再进入逐单元生产。

正式 Prompt 只能包含目标 SKU 证据和批准的抽象视觉特征，不包含参考商品、第三方人物、原文案、Logo、包装、专属符号或独特坐标。

## 质检与断点续作

迁移质检至少包含：

- `rights_status` 是否支持所选 M1/M2/M3。
- 每个目标模块是否绑定真实 SKU 证据。
- 是否错误继承来源平台规则。
- 是否出现参考商品、品牌、人物、文案、独特符号或可识别复刻。
- 商品身份是否符合 `IDENTITY_CONTRACT`，F2 是否进入人工审核。
- 三个方向是否达到至少三个维度差异。
- 批准状态是否与生产阶段一致。

把 `reference_migration_context` 保存在权威 `SKU_CONTEXT.json`。恢复时复用已完成的分段、抽象、映射、拒绝方向和批准状态；仅在参考文件改变、权利状态改变、目标平台改变或真实 SKU 证据更新影响映射时重算相关部分。更新权威状态时递增 `workflow_state.state_revision`，不得让导出视图反向覆盖它。
