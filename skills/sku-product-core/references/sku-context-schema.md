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
  evidence_sources: []
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
      current_stage: platform_planning
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
  current_stage: intake
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
  human_review_required: false
```

## F0–F3 模式

- `F0` 证据原图：真实照片或忠实精修，适合主图、SKU 图、包装和声明证据。
- `F1` 像素保留合成：真实产品像素不重绘，允许重新导演背景、光线、阴影、道具和版式。
- `F2` 身份条件编辑 / 重构：用多视图、蒙版和身份锚点生成新机位、佩戴或场景；只用于允许槽位并强制人工身份审核。
- `F3` 概念探索：用于方向和视觉实验，不能作为真实销售 SKU 成品。

## 合并规则

1. 平台 Skill 继承 `facts`、`identity_contract` 和 `creative_context`，不得无证据覆盖。
2. 新证据可以把谨慎推断升级为事实，但必须记录来源。
3. 用户切换平台时只替换 `target`，保留产品身份和事实。
4. 多平台任务共享顶层事实、身份合同和基础创意上下文，并在 `platform_contexts` 中为每个平台/站点保存独立 target、方向、生产、流程和 QA 状态；`active_platform_context_id` 指向当前工作项。顶层单数 `target` / `production` 只用于单平台项目或内存中的当前平台投影视图，不得覆盖其他平台状态。
5. 任何默认值都写入 `confirmed_assumptions`，不能伪装成用户事实。
6. 处理模式按素材槽位决定，不用一个全局模式压制整页；平台限制始终优先。
7. 恢复旧项目时保留 V1 已确认事实，只补充身份合同、创意上下文和工作流状态。

## 持久化合同

1. 项目中的 `01-context/SKU_CONTEXT.json` 是 `SKU_CONTEXT V2` 的唯一权威副本；身份合同、创意上下文、目标、方向和生产状态都保存在这个对象内。
2. `IDENTITY_CONTRACT.json`、`CREATIVE_CONTEXT.json` 和 `reference-abstraction.json` 是可选导出视图；`project-state.json` 是可选索引。它们不得反向覆盖 `SKU_CONTEXT.json`。
3. 每次成功写回递增 `workflow_state.state_revision`。可选索引必须记录同一 `state_revision`；落后时忽略并重建，超前或同版本冲突时进入人工审核。
4. 写回时先验证完整对象，再使用临时文件替换权威文件，最后刷新可选视图。恢复时先验证权威文件并找第一个未完成阶段；方向批准前不得使用预填的 `resume_from` 或 `planned_units` 越过确认门，进入生产阶段后才恢复具体单元。
5. 多平台项目的每个平台进度只写入对应 `platform_contexts[].workflow_state`；全局 `workflow_state.state_revision` 仍是整个权威文件的并发版本。切换活动平台只改变 `active_platform_context_id`，不得删除或重置其他平台上下文。
