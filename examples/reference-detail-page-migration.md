# 参考详情页迁移示例

这个示例演示：用户有一副真实墨镜的多视图产品图，同时上传一张竞品淘宝详情长图，希望生成 Amazon US 的 Listing Images 与 A+。参考页只用于竞品研究，因此不能使用 M2。

## 调用

```text
请启动 kero-sku-director。

真实 SKU 产品图：00-inputs/originals/
参考详情页：00-inputs/references/competitor-taobao-long-page.jpg
参考权利：竞品研究
目标平台：Amazon US

请使用 sku-reference-migration 先拆解参考页，建立 M1/M2/M3 判断和模块证据映射，
再给三个差异化迁移方向。我确认前不要输出正式生产 Prompt。
```

## 第一步：来源与权利结论

```yaml
source:
  files: [competitor-taobao-long-page.jpg]
  source_platform: Taobao
  source_page_type: competitor-long-page
  rights_status: competitor-analysis
  reference_role: analysis-only

mode_decision:
  forbidden: M2
  allowed: [M1, M3]
  recommended: M3
  reason: 参考页属于第三方竞品；只保留购买问题和叙事方法，重新导演视觉世界。
```

## 第二步：语义模块地图

| 参考模块 | 购买问题 | 可抽象的方法 | 必须排除 |
|---|---|---|---|
| REF-01 首屏 | 这是什么、为什么值得看 | 高反差开场、单一核心承诺 | 竞品墨镜、模特、Logo、原文案 |
| REF-02 场景利益 | 在什么环境下使用 | 场景到利益的叙事关系 | 无证据的防护功效与场景结果 |
| REF-03 结构细节 | 做工是否可靠 | 全景—细节—证据的镜头节奏 | 竞品铰链、参数与材质声明 |
| REF-04 规格收束 | 我会收到什么 | 购买确定性收束 | 竞品尺寸、包装与赠品 |

## 第三步：目标平台映射

```yaml
migration_id: MIG-AMZ-US-001
target_platform_context_id: amazon-us
migration_mode: M3
module_mapping:
  - source_module_id: REF-01
    target_unit_id: AMZ-MAIN-01
    action: replace
    target_slot: Amazon Main Image
    target_evidence_ids: [IMG-FRONT]
    handling_mode: F0
    transferable_abstract_features: [immediate product recognition]
    excluded_reference_elements: [competitor product, model, logo, source copy]
    platform_override: white background, no text overlay, real SKU only

  - source_module_id: REF-02
    target_unit_id: AMZ-SECONDARY-02
    action: adapt
    target_slot: Amazon secondary image
    target_evidence_ids: [IMG-FRONT, IMG-SIDE, FACT-USE-APPROVED]
    handling_mode: F1
    transferable_abstract_features: [scene-to-benefit narrative]
    excluded_reference_elements: [competitor scene, unverified protective claim]

  - source_module_id: REF-03
    target_unit_id: AMZ-A+-03
    action: adapt
    target_slot: Amazon A+ module
    target_evidence_ids: [IMG-HINGE, IMG-TEMPLE]
    handling_mode: F1
    transferable_abstract_features: [wide-to-macro proof rhythm]
    excluded_reference_elements: [competitor hinge, source parameters]

  - source_module_id: REF-04
    target_unit_id: AMZ-A+-04
    action: replace
    target_slot: Amazon A+ comparison or package module
    target_evidence_ids: []
    status: blocked
    platform_override: wait for verified dimensions and package contents
```

关键点：淘宝长图的宽高、模块数和叠字方式没有被复制。Amazon Main Image 被平台规则强制改为 F0；缺少包装事实的单元被阻塞，而不是从竞品页面抄数字。

## 第四步：三个迁移方向

1. `D1 精密建筑光影`：墨镜作为工程对象；硬轮廓光、建筑阴影、测量网格、识别—结构—证据节奏。
2. `D2 城市晨间适配`：墨镜作为日常伙伴；自然窗光、编辑式字幕、场景—利益—细节节奏。
3. `D3 材质感官实验室`：墨镜作为触感标本；掠射微距光、稀疏标本标签、材质—结构—身份节奏。

三个方向在创意命题、场景世界、商品角色、镜头光线、图形系统和叙事节奏上均明显不同，不是只换背景色。

## 第五步：确认后继续

```text
确认 D1。
请把 MIG-AMZ-US-001 交给 sku-amazon，按 Amazon US 的实际素材槽位继续。
逐单元记录 migration_id、source_module_id、迁移抽象特征、排除元素、平台覆盖项和原创性检查。
对 blocked 单元保留占位，不要编造包装和尺寸。
```

批准后才输出完整 Prompt 与 Negative Prompt。权威状态保存于 `01-context/SKU_CONTEXT.json` 的 `reference_migration_context`；可选的 `REFERENCE_MIGRATION_CONTEXT.json` 仅用于阅读，不能反向覆盖权威状态。
