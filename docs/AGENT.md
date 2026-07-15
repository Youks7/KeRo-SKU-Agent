# KeRo SKU Agent 使用指南

KeRo SKU Agent 是现有 KeRo SKU Skills 之上的 Codex 自定义 Agent 编排层。它不替代十个 Skills，也不把平台规则复制进 Agent 配置；它负责统一入口、状态延续、Skill 路由、方向确认门和项目文件边界。

## 组成

```text
kero-sku-director Agent
├── sku-detail-page-director
├── sku-product-core
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
- Agent 没有自带的永久数据库。跨任务继续工作时，应读取项目目录中的 `SKU_CONTEXT.json` 和 `project-state.json`。

## Agent 能做什么

1. 盘点真实产品图、包装图、规格资料和品牌资产。
2. 区分已确认事实、谨慎推断、禁止主张和缺失证据。
3. 建立并复用 `SKU_CONTEXT`，选择严格保真、AI 辅助或概念生成模式。
4. 识别平台、站点和素材槽位，只加载命中的平台 Skill。
5. 给出二至三个商业任务不同的方向，并等待用户确认。
6. 方向确认后生成逐素材 Prompt、Negative Prompt、排版说明和质检要求。
7. 把上下文、方向、Prompt 和质检报告保存到用户指定项目目录。
8. 对生成结果做产品一致性、事实边界和平台适配检查。

Agent 是否能直接生图、排版或操作电商后台，取决于当前 Codex 任务是否连接了相应工具和是否获得授权。没有生产工具时，它交付制作规范与 Prompt，不会假装完成外部操作。

## 安装

Windows PowerShell：

```powershell
git clone https://github.com/Youks7/KeRo-SKU-Agent.git
Set-Location .\KeRo-SKU-Agent
.\scripts\install_kero_sku.ps1
```

安装器把 Agent 和十个 Skills 安装到当前用户的 Codex 目录：

```text
%CODEX_HOME%\agents\kero-sku-director.toml
%CODEX_HOME%\skills\sku-detail-page-director\
%CODEX_HOME%\skills\sku-product-core\
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

请先完成产品事实分析、保真模式判断、平台识别和方向提案。
不要编造规格、材质、认证、功效或评价。
方向确认前不要输出正式生图 Prompt。
```

继续已有项目：

```text
请启动 kero-sku-director Agent。

继续项目：D:\KeRo-SKU-Projects\KE-2026-001
先读取 01-context\SKU_CONTEXT.json 和 project-state.json，
复用已确认事实，从当前未完成阶段继续。
```

## 项目文件应该放在哪里

不要把产品素材或项目结果放进 Agent、Skill 或插件安装目录。推荐每个 SKU 使用独立项目：

```text
KE-2026-001\
├── 00-inputs\
│   ├── originals\
│   ├── packaging\
│   ├── documents\
│   └── brand-assets\
├── 01-context\
│   ├── SKU_CONTEXT.json
│   └── project-state.json
├── 02-directions\
├── 03-prompts\
├── 04-generated\
├── 05-layout\
├── 06-final\
└── 07-qa\
```

原始产品素材默认只读。生成稿、排版稿和最终稿必须进入各自目录，不得覆盖 `00-inputs/originals`。

## 验证

```powershell
python scripts/validate_agent.py
```

该验证检查：

- Agent TOML 必填字段；
- 十个 Skill 依赖；
- 事实边界与方向确认门；
- 缺失 Skill 的失败行为；
- 项目文件隔离；
- 安装器依赖声明。

行为合同位于 [`tests/agent_cases.yaml`](../tests/agent_cases.yaml)。静态验证不能替代真实模型行为评审；发布前仍应在全新 Codex 任务中运行代表性案例。
