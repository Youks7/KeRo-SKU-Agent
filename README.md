# SKU 详情页导演 Skill Lite V1.2.1

> 上传真实产品图 → 深度分析产品与保真风险 → 选择详情页方向 → 输出防同质化分屏方案与生图 Prompt

这是一个面向电商运营、设计师和 AIGC 创作者的 Codex Skill。它不会一上来就生成一套不可控的详情页，而是用三阶段流程先看懂产品、再让用户选择方向，最后才输出可执行的分屏 Prompt。

## 它能做什么

### 1. 产品深度分析

识别图片中可以确认的事实、需要谨慎表达的信息和绝对不能编造的内容，并根据真实 SKU 风险推荐产品处理模式。

### 2. 三种详情页方向

提供功能转化、场景种草、高端质感等三个明显不同的策略，描述未来每一屏大概长什么样，并明确推荐方向。

### 3. 确认后生成分屏 Prompt

用户确认方向后，输出每屏销售任务、画面、文案方向、镜头矩阵、Prompt、Negative Prompt、产品处理要求、文字安全区和质检点。

### 4. 防同质化生产

先扫描类目模板套路，再从产品自身提炼视觉记忆点；每屏 Prompt 必须包含至少两个产品专属细节，避免“产品 + 高级背景 + 柔光留白”的通用模板。

## 三种产品处理模式

- **模式 A：严格保真** — 真实产品抠图合成，AI 只生成背景、光影和场景。
- **模式 B：AI 辅助商品图** — 基于真实产品参考图做背景替换、光影优化或轻度重绘，并执行一致性质检。
- **模式 C：概念生成** — 仅用于新品提案和方向测试，不可当作真实 SKU 成品图。

## 适用平台

淘宝、天猫、京东、拼多多、抖音商城、小红书、Amazon、Shopify、TikTok Shop 等国内外电商平台。

## 怎么使用

### 在 Codex 中使用

1. 下载仓库中的 `SKU详情页导演Skill.skill`。
2. 将 Skill 导入 Codex，或把 `sku-detail-page-director/` 整个目录复制到 Codex 的 skills 目录。
3. 在 Codex 中说：“使用 `$sku-detail-page-director` 帮我分析这个产品并做详情页。”
4. 按引导上传真实产品图并选择方向。

### 在 Agent 项目中使用

复制 `SKU详情页导演Skill/sku-detail-page-director/` 整个目录。`SKILL.md` 负责触发和阶段路由，`references/` 中保留 V1.2.1 完整权威规则。

## 项目结构

```text
SKU详情页导演Skill/
├── sku-detail-page-director/
│   ├── SKILL.md
│   ├── agents/
│   │   └── openai.yaml
│   └── references/
│       └── SKU详情页导演Skill_Lite_V1.2.1_防同质化生产优化版.md
└── SKU详情页导演Skill.skill
```

## 版本

当前版本：Lite V1.2.1 防同质化生产优化版。

原始规则文件保持完整收录；仓库化改造仅补充 Codex Skill 元数据、触发路由、UI 配置、说明文档与可导入包。

---

## 关于我

**秋水 Kero**，AIGC 创作者，喜欢折腾，也喜欢体验新鲜事物。

X（推特）：[@Isonlyonenice](https://x.com/Isonlyonenice)

持续分享 AI、图片与各种有趣的新鲜玩法。
