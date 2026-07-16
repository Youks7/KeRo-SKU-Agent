# KeRo SKU Agent 使用指南

KeRo SKU Agent 是现有 KeRo SKU Skills 之上的 Codex 自定义 Agent 编排层。它不替代十一个 Skills，也不把平台规则复制进 Agent 配置；它负责产品图诊断、身份合同、参考页迁移、创意方向、状态延续、Skill 路由、方向确认门和项目文件边界。

## 组成

```text
kero-sku-director Agent
├── sku-detail-page-director
├── sku-product-core
├── sku-reference-migration
├── sku-taobao
├── sku-tmall
├── sku-pinduoduo
├── sku-jd
├── sku-1688
├── sku-amazon
├── sku-shopify
└── sku-tiktok-shop
```

- `.codex/agents/kero-sku-director.toml` 是真正的自定义 Agent 配置。
- 每个 Skill 内的 `agents/openai.yaml` 只是 Skill 的界面元数据，不是自定义 Agent。
- Agent 没有自带的永久数据库。跨任务继续工作时，以项目目录中的 `01-context/SKU_CONTEXT.json` 为唯一权威状态；它已经包含身份合同、创意上下文、参考迁移上下文、方向和生产进度。其他 context JSON 只能是可选导出视图或索引。

## Agent 能做什么

1. 盘点真实产品图、包装图、规格资料和品牌资产。
2. 区分已确认事实、谨慎推断、禁止主张和缺失证据。
3. 诊断产品图并建立多视图证据、`SKU_CONTEXT V2` 和 `IDENTITY_CONTRACT`。
4. 对参考详情页做语义分段、权利判断和 M1/M2/M3 选择，为目标 SKU 建立证据绑定的模块映射。
5. 识别平台、站点和素材槽位，为每个槽位选择 F0–F3。
6. 建立 `CREATIVE_CONTEXT`，给出三个差异化方向并等待用户确认。
7. 方向确认后按“策划—提示词—生成”分层，生成逐素材 Prompt、Negative Prompt、身份锚点、排版说明和质检要求。
8. 把上下文、方向、Prompt 和质检报告保存到用户指定项目目录，并支持断点续作。
9. 对生成结果做事实、商品身份、创意质量、参考边界和平台适配检查。

### F0–F3

- F0：证据原图或忠实精修。
- F1：保留真实产品像素，重新导演场景、光影和版式。
- F2：用多视图、蒙版和身份锚点进行新机位、佩戴或场景重构，强制人工审核。
- F3：概念探索，不可直接发布。

Agent 是否能直接生图、排版或操作电商后台，取决于当前 Codex 任务是否连接了相应工具和是否获得授权。没有生产工具时，它交付制作规范与 Prompt，不会假装完成外部操作。

## 安装

Windows PowerShell：

```powershell
git clone https://github.com/Youks7/KeRo-SKU-Agent.git
Set-Location .\KeRo-SKU-Agent
.\scripts\install_kero_sku.ps1
```

安装器把 Agent 和十一个 Skills 安装到当前用户的 Codex 目录：

```text
%CODEX_HOME%\agents\kero-sku-director.toml
%CODEX_HOME%\skills\sku-detail-page-director\
%CODEX_HOME%\skills\sku-product-core\
%CODEX_HOME%\skills\sku-reference-migration\
...其余八个平台 Skills
```

未设置 `CODEX_HOME` 时，默认使用：

```text
%USERPROFILE%\.codex
```

如果已安装文件与仓库版本不同，安装器会停止，不会静默覆盖。确认需要更新时使用：

```powershell
.\scripts\install_kero_sku.ps1 -Force
```

`-Force` 会先把不同版本移动到：

```text
%CODEX_HOME%\backups\kero-sku\时间戳\
```

安装后新建 Codex 任务；仍未发现 Agent 时再重启 Codex。

## 第一次调用

```text
请启动 kero-sku-director Agent。

项目目录：D:\KeRo-SKU-Projects\KE-2026-001
原始产品资料在 00-inputs。

请先完成产品图诊断、多视图统一、事实分析、身份合同、参考页抽象、平台识别和三套创意方向。
不要编造规格、材质、认证、功效或评价。
商品身份必须真实，但不要把所有详情素材限制成同一张原图抠图；按槽位选择 F0–F3。
方向确认前不要输出正式生图 Prompt。
```

迁移参考详情页：

```text
请启动 kero-sku-director Agent。

真实 SKU 资料：D:\KeRo-SKU-Projects\KE-2026-001\00-inputs\originals
参考详情页：D:\KeRo-SKU-Projects\KE-2026-001\00-inputs\references
参考权利：我的旧页面 / 已授权 / 竞品研究 / 不确定
目标平台：Amazon US

请使用 sku-reference-migration 做语义分段、权利判断、参考抽象和模块证据映射，
选择 M1、M2 或 M3，并给出三个差异化迁移方向。确认前不要输出正式生产 Prompt。
```

继续已有项目：

```text
请启动 kero-sku-director Agent。

继续项目：D:\KeRo-SKU-Projects\KE-2026-001
先读取并验证唯一权威状态 01-context\SKU_CONTEXT.json。
可选 project-state.json 只有在 state_revision 一致时才能作索引；落后时忽略并重建。
复用已确认事实、参考分段、模块映射与方向，先恢复第一个未完成阶段；方向批准后才进入 resume_from 或未完成生产单元。
```

## 项目文件应该放在哪里

不要把产品素材或项目结果放进 Agent、Skill 或插件安装目录。推荐每个 SKU 使用独立项目：

```text
KE-2026-001\
├── 00-inputs\
│   ├── originals\
│   ├── packaging\
│   ├── documents\
│   ├── brand-assets\
│   └── references\
├── 01-context\
│   ├── SKU_CONTEXT.json
│   ├── IDENTITY_CONTRACT.json        # 可选导出视图
│   ├── CREATIVE_CONTEXT.json         # 可选导出视图
│   ├── REFERENCE_MIGRATION_CONTEXT.json # 可选导出视图
│   ├── reference-abstraction.json    # 可选导出视图
│   └── project-state.json            # 可选索引
├── 02-directions\
├── 03-prompts\
├── 04-generated\
├── 05-layout\
├── 06-final\
└── 07-qa\
```

原始产品素材默认只读。生成稿、排版稿和最终稿必须进入各自目录，不得覆盖 `00-inputs/originals`。

### 状态写回与恢复

1. 先在内存中合并并验证完整 `SKU_CONTEXT V2`。
2. 递增 `workflow_state.state_revision`，再原子替换 `SKU_CONTEXT.json`。
3. 权威文件写入成功后才刷新导出视图和 `project-state.json`。
4. 恢复时权威文件优先；索引落后就忽略，索引超前或同版本冲突就进入人工审核。
5. 先恢复第一个未完成阶段，绝不让预填 `resume_from` 或 `planned_units` 越过方向确认门；进入生产阶段后，才从 `planned_units` 找第一个未完成单元。
6. 多平台项目分别写入 `platform_contexts`，用 `active_platform_context_id` 选择当前平台；参考页的来源分段全局复用，各平台的迁移映射分别写入 `reference_migration_context.platform_migrations`。

## 验证

```powershell
python scripts/validate_agent.py
python scripts/validate_creative_system.py
python scripts/validate_reference_migration.py
python scripts/validate_resume_state.py
python scripts/validate_production_protocol.py
```

该验证检查：

- Agent TOML 必填字段；
- 十一个 Skill 依赖；
- 事实边界与方向确认门；
- 缺失 Skill 的失败行为；
- 项目文件隔离；
- 安装器依赖声明。
- F0–F3 槽位路由、三个差异化方向和墨镜身份锚点回归。
- M1/M2/M3 权利边界、模块证据映射、跨平台重排和迁移方向确认门。
- 单一权威状态的版本优先级和断点恢复。

行为合同位于 [`tests/agent_cases.yaml`](../tests/agent_cases.yaml)，创意回归位于 [`tests/creative-direction/sunglasses-directions.yaml`](../tests/creative-direction/sunglasses-directions.yaml)，真实外部素材记录位于 [`tests/real-sku/REAL_SUNGLASSES_REGRESSION.md`](../tests/real-sku/REAL_SUNGLASSES_REGRESSION.md)。静态验证和真实输入检查不能替代对实际生成结果的人工身份审核；发布前仍应在全新 Codex 任务中运行代表性案例。
