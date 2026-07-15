# KeRo SKU Director Agent

面向真实商品资料的 Codex 电商项目总导演：先建立产品事实，再选择平台工作流，确认方向后才进入 Prompt、排版和质检。

> 这是一个 **Agent 仓库**，不是原 [`KeRo-SKU-skill`](https://github.com/Youks7/KeRo-SKU-skill) 的同名镜像。仓库保留原有十个 SKU Skills 作为专业能力层，并增加 `kero-sku-director` 自定义 Agent、安装器、行为验证和项目状态规则。

## 先看结论

- 只需要记住一个调用名称：`kero-sku-director`。
- Windows 已提供并验证 PowerShell 安装器。
- macOS 当前采用手动复制安装，不应运行 Windows 安装器。
- Agent 和 Skills 安装在用户的 Codex 目录；商品资料放在单独的 SKU 项目目录。
- Agent 不会在后台自行运行，也不会在缺少工具时假装已经生图、排版或操作电商后台。

## Agent 负责什么

`kero-sku-director` 是十个 Skills 之上的编排层，负责：

1. 盘点产品图、包装图、规格文件和品牌资产。
2. 把信息分为已确认事实、谨慎推断、缺失证据和禁止主张。
3. 建立并复用 `SKU_CONTEXT`，避免每轮重新分析产品。
4. 根据淘宝、天猫、拼多多、京东、1688、Amazon、Shopify 或 TikTok Shop 选择对应 Skill。
5. 先提出二至三个商业方向，等待用户确认。
6. 方向确认后生成逐素材 Prompt、Negative Prompt、排版要求和质检清单。
7. 检查颜色、结构、比例、Logo、包装文字和产品主张是否失真。
8. 把上下文、方向和交付结果写入用户指定的项目目录。

```text
真实产品资料
  -> 产品事实与保真分析
  -> 平台和素材槽位识别
  -> 方向提案与人工确认
  -> Prompt / 排版 / 生产
  -> 产品一致性与事实边界质检
```

## 安装内容

安装完成后应存在一个 Agent 和十个 Skills：

```text
kero-sku-director
sku-detail-page-director
sku-product-core
sku-taobao
sku-tmall
sku-pinduoduo
sku-jd
sku-1688
sku-amazon
sku-shopify
sku-tiktok-shop
```

Codex 使用 `CODEX_HOME` 作为安装根目录。未设置时，通常使用当前用户主目录下的 `.codex`。

## Windows：发送给 Codex 的安装指令

在新 Windows 电脑中安装并登录 Codex，新建任务，然后完整发送下面这段话：

```text
我的电脑是 Windows。

请安装这个公开仓库中的 Codex 自定义 Agent：
https://github.com/Youks7/KeRo-SKU-Agent

请执行以下操作：

1. 下载或克隆仓库 main 分支。
2. 阅读 docs/INSTALL.md 和 docs/AGENT.md。
3. 确认 .codex/agents/kero-sku-director.toml 存在。
4. 在仓库根目录运行：
   .\scripts\install_kero_sku.ps1
5. 如果 PowerShell 执行策略阻止脚本，只对本次安装使用：
   powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\install_kero_sku.ps1
6. CODEX_HOME 未设置时，安装到 %USERPROFILE%\.codex。
7. 需要访问网络或写入用户 .codex 目录时，向我申请权限。
8. 已安装相同版本时跳过；存在不同版本时停止并报告，不要直接覆盖。
9. 验证 kero-sku-director Agent 和十个 sku-* Skill 全部存在。
10. 验证每个 Skill 目录中都存在 SKILL.md。
11. 不要把商品图片或 SKU 项目数据写进 Agent、Skill 或插件安装目录。
12. 最后报告实际 CODEX_HOME、安装位置、十一项验证结果和是否需要重启 Codex。
13. 如果失败，请返回真实错误，不要假装安装成功。
```

也可以由用户自己在 PowerShell 中执行：

```powershell
git clone https://github.com/Youks7/KeRo-SKU-Agent.git
Set-Location .\KeRo-SKU-Agent
.\scripts\install_kero_sku.ps1
```

Windows 默认安装位置：

```text
C:\Users\<用户名>\.codex\agents\kero-sku-director.toml
C:\Users\<用户名>\.codex\skills\<skill-name>\
```

## macOS：发送给 Codex 的安装指令

仓库当前没有 macOS 自动安装脚本。请让 Codex 安全复制文件，而不是运行 `.ps1`：

```text
我的电脑是 macOS。

请安装这个公开仓库中的 Codex 自定义 Agent：
https://github.com/Youks7/KeRo-SKU-Agent

请执行以下操作：

1. 下载或克隆仓库 main 分支。
2. 阅读 docs/INSTALL.md 和 docs/AGENT.md。
3. 不要运行 scripts/install_kero_sku.ps1；它是 Windows 安装器。
4. 先解析统一的目标目录 TARGET_CODEX_HOME：CODEX_HOME 已设置时使用其值；未设置时使用 $HOME/.codex。
5. 如有需要，创建 $TARGET_CODEX_HOME/agents 和 $TARGET_CODEX_HOME/skills。
6. 把仓库中的 .codex/agents/kero-sku-director.toml 复制到：
   $TARGET_CODEX_HOME/agents/kero-sku-director.toml
7. 在仓库中查找并完整复制以下十个 Skill 目录到 $TARGET_CODEX_HOME/skills：
   sku-detail-page-director
   sku-product-core
   sku-taobao
   sku-tmall
   sku-pinduoduo
   sku-jd
   sku-1688
   sku-amazon
   sku-shopify
   sku-tiktok-shop
8. sku-detail-page-director 的上级目录名称可能包含中文。不要依赖固定中文路径；通过查找 sku-detail-page-director/SKILL.md 定位。
9. 需要访问网络或写入 $TARGET_CODEX_HOME 时，向我申请权限。
10. 已安装相同版本时跳过；存在不同版本时停止并报告，不要直接覆盖或删除。
11. 验证 Agent 文件和十个 Skill 的 SKILL.md 全部存在。
12. 不要把商品图片或 SKU 项目数据写进 Agent、Skill 或插件安装目录。
13. 最后报告实际 CODEX_HOME、安装位置、十一项验证结果和是否需要重启 Codex。
14. 如果当前环境不支持个人自定义 Agent，请明确报告原因，不要假装安装成功。
```

macOS 默认安装位置：

```text
/Users/<用户名>/.codex/agents/kero-sku-director.toml
/Users/<用户名>/.codex/skills/<skill-name>/
```

## 安装后如何启动

安装完成后先新建一个 Codex 任务。若新任务仍找不到 Agent，再完全退出并重新启动 Codex。

第一次处理 SKU 时发送：

```text
请启动并把任务委派给 kero-sku-director 自定义 Agent。

如果找不到这个 Agent，请停止并明确报告，不要在主 Agent 中模拟它已经运行。

项目目录：[填写项目目录]
目标平台：[填写平台和站点]
原始产品资料位于：[填写资料目录]

请先完成：
1. 产品资料盘点；
2. 产品事实分析；
3. 建立 SKU_CONTEXT；
4. 判断保真模式；
5. 调用对应平台 Skill；
6. 提供三个商业任务不同的详情页方向。

不得编造品牌、规格、尺寸、材质、认证、功效、评价、销量、价格或售后承诺。
方向确认前不要生成正式生产 Prompt，也不要写入最终交付目录。
```

选定方向后发送：

```text
确认方向 [填写编号]。

请继续使用 kero-sku-director Agent，生成：
1. 平台素材槽位规划；
2. 逐素材 Prompt；
3. Negative Prompt；
4. 产品处理模式；
5. 文案位置与信息层级；
6. 后期排版要求；
7. 产品一致性质检清单。

结果保存到当前 SKU 项目目录，不要覆盖原始素材。
```

继续已有项目时发送：

```text
请启动并把任务委派给 kero-sku-director 自定义 Agent。

继续项目：[填写项目目录]

先读取 01-context/SKU_CONTEXT.json 和 01-context/project-state.json，
复用已经确认的事实，从未完成阶段继续。
如果找不到 Agent 或状态文件，请明确报告，不要模拟已经读取。
```

## 商品项目应该放在哪里

GitHub 仓库和 `.codex` 保存能力源码；每个真实 SKU 使用独立项目目录：

```text
KE-2026-001/
├── 00-inputs/
│   ├── originals/
│   ├── packaging/
│   ├── documents/
│   └── brand-assets/
├── 01-context/
│   ├── SKU_CONTEXT.json
│   └── project-state.json
├── 02-directions/
├── 03-prompts/
├── 04-generated/
├── 05-layout/
├── 06-final/
└── 07-qa/
```

`00-inputs/originals` 默认只读。生成稿、排版稿和最终稿进入各自目录，不覆盖、不移动、不重命名原始产品资料。

## 能力边界

- Agent 是 Codex 自定义会话配置和流程总导演，不是常驻后台服务。
- Agent 没有自带永久数据库；跨任务状态来自项目目录中的 JSON 文件。
- 没有图像生产工具时，只交付 Prompt 和制作规范。
- 没有授权的浏览器、MCP 或平台工具时，不能操作电商后台。
- 目标平台 Skill 缺失时必须报告，不能模拟不存在的完整平台规则。
- 竞品只能用于研究构图、节奏和信息结构，不能复制产品、Logo、文案或品牌资产。

## 更新已经安装的版本

先拉取仓库更新，再运行安装器。Windows 可以执行：

```powershell
Set-Location .\KeRo-SKU-Agent
git pull origin main
.\scripts\install_kero_sku.ps1 -Force
```

`-Force` 会先把不同版本备份到 `%CODEX_HOME%\backups\kero-sku\<时间戳>\`。macOS 更新时仍应先比较和备份现有目录，再复制新版本。

## 验证仓库

```powershell
python scripts/validate_agent.py
python scripts/validate_all_skills.py
python scripts/validate_trigger_cases.py
```

验证覆盖 Agent 必填字段、十个 Skill 依赖、方向确认门、缺失 Skill 行为和项目文件隔离。静态验证不等于真实模型行为评审，发布前仍应在全新 Codex 任务中运行代表性案例。

## 继续阅读

- [Agent 完整指南](./docs/AGENT.md)
- [安装与更新](./docs/INSTALL.md)
- [常见问题](./docs/TROUBLESHOOTING.md)
- [安全与使用边界](./docs/SAFETY_AND_USAGE.md)
- [行为场景](./tests/agent_cases.yaml)
- [版本记录](./CHANGELOG.md)

## 许可与作者

使用和再发布前请阅读 [LICENSE](./LICENSE) 与 [NOTICE.md](./NOTICE.md)。第三方平台名称、商标、产品和工具名称归各自权利人所有。

作者：**秋水 Kero**

X：[@Isonlyonenice](https://x.com/Isonlyonenice)
