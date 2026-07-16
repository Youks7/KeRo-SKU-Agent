# SKU_CONTEXT V2

使用下面的 YAML 结构在公共核心、创意导演、路由和平台 Skill 之间传递状态。V2 兼容 V1 的事实字段；旧项目缺少的新字段保持为空并按需补齐，不得猜测填充。

## 目录

- [标准结构](#标准结构)
- [F0–F3 模式](#f0f3-模式)
- [合并规则](#合并规则)

## 标准结构

```yaml
sku_context_version: 2

product_identity:
  category: null
  product_name: null
  source_images: []
  source_image_roles: []
  view_confidence: {}
  visible_structure: []
  primary_colors: []
  included_items: []
  packaging: null
  logo_status: null

facts:
  verified: []
  cautious_inferences: []
  prohibited_claims: []
  missing_evidence: []
  evidence_sources:
    - evidence_id: null
      source_type: null  # real-sku-image / verified-document / user-confirmed-fact
      source_ref: null
  claim_evidence_map: []

# IDENTITY_CONTRACT：锁定真实 SKU 身份，不锁死所有原图像素。
identity_contract:
  immutable_traits: []
  bounded_traits: []
  unknown_traits: []
  allowed_transformations: []
  prohibited_transformations: []
  identity_landmarks: []
  variant_delivery_map: []

visual_memory_points:
  - point: null
    product_evidence: null
    suitable_uses: []

# CREATIVE_CONTEXT：事实稳定后建立，方向批准前不得进入正式生产。
creative_context:
  business_goal: null
  target_audience: null
  purchase_barrier: null
  desired_customer_feeling: null
  product_truth_to_dramatize: []
  creative_thesis: null
  product_role: null
  visual_world: null
  camera_grammar: []
  lighting_grammar: []
  material_grammar: []
  graphic_system: []
  narrative_arc: []
  cliches_to_avoid: []
  reference_abstraction_reports: []
  directions: []
  selected_direction: null
  rejected_directions: []
  approval_status: pending

# REFERENCE_MIGRATION_CONTEXT：参考页只提供方法与视觉语言，不提供商品事实。
# 全局保存来源、分段与抽象；每个目标平台拥有独立迁移映射和批准状态。
reference_migration_context:
  version: 1
  source:
    files: []
    source_platform: null
    source_page_type: null
    rights_status: unknown  # self-owned / authorized / competitor-analysis / unknown
    reference_role: analysis-only
  semantic_modules:
    - source_module_id: null
      source_region: null
      module_role: null
      customer_question: null
      information_type: null
      composition: []
      camera: []
      lighting: []
      material: []
      graphic_system: []
      narrative_position: null
      protected_or_unique_elements: []
      reusability: method-only
  reference_visual_tokens:
    composition_grammar: []
    camera_grammar: []
    lighting_grammar: []
    material_grammar: []
    graphic_grammar: []
    narrative_grammar: []
  excluded_elements: []
  platform_migrations:
    - migration_id: null
      target_platform_context_id: null
      migration_mode: null  # M1 / M2 / M3
      migration_intensity: null
      module_mapping:
        - source_module_id: null
          target_unit_id: null
          action: adapt  # keep / adapt / replace / discard
          target_slot: null
          target_customer_question: null
          target_evidence_ids: []
          handling_mode: null  # F0 / F1 / F2 / F3
          transferable_abstract_features: []
          excluded_reference_elements: []
          platform_override: null
          status: planned
      # 目标平台必需、但不由参考模块迁移而来的真实组件或资产。
      platform_native_units:
        - target_unit_id: null
          target_slot: null
          reason: null
          target_evidence_ids: []
          status: planned
      migration_directions: []
      selected_direction: null
      rejected_directions: []
      approval_status: pending
      qa:
        rights_status: null
        evidence_binding_status: null
        originality_status: null
        platform_remap_status: null
        human_review_required: false

production:
  default_handling_mode: null  # F0 / F1 / F2 / F3
  handling_reason: null
  creative_freedom_by_slot: {}
  tool_capabilities: []
  source_and_mask_plan: []
  allowed_edits: []
  prohibited_edits: []
  fidelity_requirements: []

target:
  platform: null
  marketplace_site: null
  language: null
  seller_type: null
  category: null
  asset_slots: []
  brand_status: null
  current_rule_source: null
  current_rule_checked_at: null

# 多平台项目的权威落盘结构。单平台项目可继续使用上面的 target / production。
platform_contexts:
  - context_id: null
    target: {}
    creative_context_overrides: {}
    direction_state:
      selected_direction: null
      rejected_directions: []
      approval_status: pending
    production: {}
    workflow_state:
      current_stage: platform_planning  # intake / product_core / reference_analysis / platform_planning / directions / direction_approval / production / qa
      completed_stages: []
      planned_units: []
      completed_units: []
      repair_tasks: []
      human_review_items: []
      resume_from: null
    qa: {}
active_platform_context_id: null

decisions:
  confirmed_assumptions: []
  pending_decision: null

workflow_state:
  state_revision: 1
  updated_at: null
  current_stage: intake  # intake / product_core / reference_analysis / platform_planning / directions / direction_approval / production / qa
  completed_stages: []
  planned_units: []
  completed_units: []
  repair_tasks: []
  human_review_items: []
  resume_from: null

qa:
  fact_status: null
  identity_status: null
  creative_quality_status: null
  platform_status: null
  reference_rights_status: null
  reference_migration_status: null
  human_review_required: false
```

## F0–F3 模式

- `F0` 证据原图：真实照片或忠实精修，适合主图、SKU 图、包装和声明证据。
- `F1` 像素保留合成：真实产品像素不重绘，允许重新导演背景、光线、阴影、道具和版式。
- `F2` 身份条件编辑 / 重构：用多视图、蒙版和身份锚点生成新机位、佩戴或场景；只用于允许槽位并强制人工身份审核。
- `F3` 概念探索：用于方向和视觉实验，不能作为真实销售 SKU 成品。

## 合并规则

1. 平台 Skill 继承 `facts`、`identity_contract`、`creative_context` 和已批准的 `reference_migration_context`，不得无证据覆盖。
2. 新证据可以把谨慎推断升级为事实，但必须记录来源。
3. 用户切换平台时只替换 `target`，保留产品身份和事实。
4. 多平台任务共享顶层事实、身份合同和基础创意上下文，并在 `platform_contexts` 中为每个平台/站点保存独立 target、方向、生产、流程和 QA 状态；`active_platform_context_id` 指向当前工作项。顶层单数 `target` / `production` 只用于单平台项目或内存中的当前平台投影视图，不得覆盖其他平台状态。
5. 任何默认值都写入 `confirmed_assumptions`，不能伪装成用户事实。
6. 处理模式按素材槽位决定，不用一个全局模式压制整页；平台限制始终优先。
7. 恢复旧项目时保留 V1 已确认事实，只补充身份合同、创意上下文、参考迁移上下文和工作流状态。
8. 参考页的来源、语义分段和抽象 Token 全局复用；每个平台的 M1/M2/M3、模块映射、方向和批准状态只写入对应 `platform_migrations[]`，并通过 `target_platform_context_id` 关联目标平台。
9. `reference_migration_context` 不是商品事实来源。任何非 `discard` 映射必须绑定 `facts` 或 `product_identity` 中的真实证据；目标平台规则覆盖来源页面做法。
10. 迁移方向批准后，`platform_migrations[].selected_direction` 必须与对应 `platform_contexts[].direction_state.selected_direction` 一致，并把方向内容投影到 `creative_context_overrides`；不得让迁移方向和平台创意方向成为两套互相冲突的权威状态。
11. 目标平台原生且不来自参考模块的组件保存到 `platform_native_units`，不得创建虚假的来源模块映射。多平台默认可共用母方向，但每个平台的选择和批准状态仍独立持久化。
12. 只要存在参考迁移，即使目标只有一个，也建立一个 `platform_contexts[]` 条目并设置 `active_platform_context_id`；每个迁移条目的 `target_platform_context_id` 必须唯一匹配它，避免单数投影视图无法保存迁移批准与断点状态。
13. `target_evidence_ids` 必须匹配 `facts.evidence_sources[].evidence_id`、`facts.verified` / `claim_evidence_map` 中的稳定事实 ID，或 `product_identity.source_images` 中的稳定图片 ID。兼容读取旧项目中的字符串来源，但新写入项目应使用带 ID 的结构；不得用未登记的占位 ID 通过证据闸门。

## 持久化合同

1. 项目中的 `01-context/SKU_CONTEXT.json` 是 `SKU_CONTEXT V2` 的唯一权威副本；身份合同、创意上下文、参考迁移上下文、目标、方向和生产状态都保存在这个对象内。
2. `IDENTITY_CONTRACT.json`、`CREATIVE_CONTEXT.json`、`REFERENCE_MIGRATION_CONTEXT.json` 和 `reference-abstraction.json` 是可选导出视图；`project-state.json` 是可选索引。它们不得反向覆盖 `SKU_CONTEXT.json`。
3. 第一份成功持久化的权威上下文使用 `workflow_state.state_revision: 1`，之后每次成功写回递增。尚未落盘的内存候选状态不是可恢复权威状态；可选索引必须记录同一 `state_revision`，落后时忽略并重建，超前或同版本冲突时进入人工审核。
4. `current_stage`、`completed_stages` 和阶段型 `resume_from` 只使用标准阶段：`intake`、`product_core`、`reference_analysis`、`platform_planning`、`directions`、`direction_approval`、`production`、`qa`；进入生产后 `resume_from` 才可以使用具体 `target_unit_id`。
5. 写回时先验证完整对象，再使用临时文件替换权威文件，最后刷新可选视图。恢复时先验证权威文件并找第一个未完成阶段；方向批准前不得使用预填的 `resume_from` 或 `planned_units` 越过确认门，进入生产阶段后才恢复具体单元。
6. 多平台项目的每个平台进度只写入对应 `platform_contexts[].workflow_state`；全局 `workflow_state.state_revision` 仍是整个权威文件的并发版本。切换活动平台只改变 `active_platform_context_id`，不得删除或重置其他平台上下文。
