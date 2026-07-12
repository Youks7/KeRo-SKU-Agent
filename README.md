<h1 align="center">KeRo SKU Skill</h1>

<p align="center"><strong>先保护真实 SKU，再做不套模板的电商详情页</strong></p>

<p align="center">真实产品保真 · 三阶段决策 · 防同质化生产 · 逐屏商业图</p>

<p align="center">
  简体中文 ·
  <a href="./README_EN.md">English</a> ·
  <a href="./README_ZH-TW.md">繁體中文</a>
</p>

<p align="center">
  <a href="./SKU详情页导演Skill/SKU详情页导演Skill.skill">下载 Skill</a> ·
  <a href="./docs/INSTALL.md">安装说明</a> ·
  <a href="./examples/sunglasses-detail-page.md">查看示例</a> ·
  <a href="./shared/core-safety.md">公共安全规则</a>
</p>

---

## 这是什么

KeRo SKU Skill 是一组用于 **真实 SKU 商品事实分析、平台路由、详情页策划与 AI 视觉生产** 的 Codex Skills。

它的核心不是让 AI 直接“发挥想象”生成商品图，而是先保护真实产品，再把电商详情页拆成可控流程：

```text
上传真实产品图
   ↓
sku-product-core：产品事实与保真分析
   ↓
kero总路由：识别平台与素材槽位
   ↓
淘宝 / 天猫 / 拼多多 / 京东 / 1688
Amazon / Shopify / TikTok Shop 专用 Skill
   ↓
平台原生素材方案、Prompt 与质检
```

V1.3 开发版不再把平台差异简化为视觉风格，而是分别处理各平台的素材槽位、商品数据、采购逻辑、网页结构和合规要求。

## V1.3 平台 Skills

| Skill | 主要职责 |
| --- | --- |
| `$sku-detail-page-director` | 平台未知、旧版兼容和多平台路由 |
| `$sku-product-core` | 事实、证据、保真模式和跨平台 `SKU_CONTEXT` |
| `$sku-taobao` | 淘宝主图、轮播、SKU 属性图和详情模块 |
| `$sku-tmall` | 天猫品牌、资质、SPU/SKU 和品牌详情 |
| `$sku-pinduoduo` | 拼多多 SKU—价格—图片一致性与详情素材 |
| `$sku-jd` | 京东参数、兼容性、包装、服务和专业详情 |
| `$sku-1688` | 1688 MOQ、阶梯价、定制、生产交付和询盘 |
| `$sku-amazon` | Amazon Main Image、附图、A+ 和 Brand Story |
| `$sku-shopify` | Shopify PDP sections、媒体、变体、SEO 和 CTA |
| `$sku-tiktok-shop` | TikTok Shop PDP、变体图、广告源图和内容交接 |

## 适合谁使用

- 电商运营：需要快速判断一个 SKU 详情页怎么做。
- 设计师：需要把产品图拆成可执行的视觉方向和分屏方案。
- AIGC 创作者：需要更安全、更稳定的商品图 Prompt。
- 跨境卖家：需要 Amazon A+、Shopify、TikTok Shop 商品图方向。
- 批量上新团队：需要避免所有 SKU 都长得像同一套模板。

## 你想做什么，直接看这里

| 你的需求 | 建议入口 |
| --- | --- |
| 第一次安装 Skill | [安装说明](./docs/INSTALL.md) |
| 不知道怎么启动 | [第一次使用](#第一次使用) |
| 想看完整流程 | [三阶段工作流](#三阶段工作流) |
| 想做淘宝 / 抖音详情页 | [淘宝 9:16 示例](./examples/taobao-9-16-detail-page.md) |
| 想做 Amazon A+ | [Amazon A+ 示例](./examples/amazon-a-plus-example.md) |
| 想看同一 SKU 的平台差异 | [V1.3 跨平台墨镜示例](./examples/cross-platform-sunglasses-v1.3.md) |
| 查看八个平台前向测试结果 | [V1.3 前向测试报告](./tests/FORWARD_TEST_REPORT.md) |
| 想做墨镜类商品图 | [墨镜详情页示例](./examples/sunglasses-detail-page.md) |
| 想参考竞品但不想侵权 | [安全参考竞品示例](./examples/competitor-reference-safe-use.md) |
| Skill 没有触发或产品变形 | [常见问题](./docs/TROUBLESHOOTING.md) |
| 想了解商用边界 | [安全与使用边界](./docs/SAFETY_AND_USAGE.md) |

## 三阶段工作流

### 阶段一：公共产品事实分析

只分析产品，不输出正式生图 Prompt。

这一阶段会判断：

- 图片里能确认的产品事实。
- 哪些信息不能编造。
- 产品适合严格保真、AI 辅助商品图，还是概念生成。
- 类目中常见的同质化套路。
- 这个产品自己的视觉记忆点。
- 下一步只需要你确认的一个关键决策。

### 阶段二：平台路由与方向提案

识别平台和素材槽位，再由对应平台 Skill 给出二至三个商业任务明显不同的方向。A/B/C 只是选择标签，不再固定等于功能、场景和高端。

每个方向会说明：

- 目标平台、地区、类目和素材槽位。
- 该平台真正需要解决的购买或采购问题。
- 页面、模块或媒体顺序。
- 未来每个素材大概长什么样。
- 如何避开常见模板感。
- 优点、风险和推荐程度。

### 阶段三：按平台素材槽位生产

只有你确认方向后，才进入主图、轮播、SKU 图、详情模块、A+、PDP section 等对应资产生产。

每一屏会包含：

- 素材槽位和商业任务。
- 构图说明。
- 文案方向。
- 生图 Prompt。
- Negative Prompt。
- 产品保真要求。
- 文字安全区或真实网页组件要求。
- 一致性质检点。

## 快速安装

### 方法一：导入 `.skill` 文件

下载 `packages/` 中对应平台的独立 `.skill` 文件，或使用合集包：

- [`V1.3 全平台合集`](./packages/kero-sku-skills-v1.3-bundle.zip)
- [`独立平台安装包目录`](./packages/)

旧地址 [`SKU详情页导演Skill.skill`](./SKU详情页导演Skill/SKU详情页导演Skill.skill) 现在是兼容路由包，不再包含所有平台的巨型规则。

### 方法二：复制 Skill 目录

把需要的平台目录复制到 Codex 的 skills 目录：

```text
SKU详情页导演Skill/sku-detail-page-director/
skills/sku-product-core/
skills/sku-amazon/
skills/sku-1688/
...只复制需要的平台
```

如果你的系统或工具对中文路径不稳定，优先复制内部的 `sku-detail-page-director/` 目录。

更详细步骤见 [docs/INSTALL.md](./docs/INSTALL.md)。

## 第一次使用

上传真实产品图后，发送：

```text
请使用 $sku-product-core 分析我上传的真实产品资料并生成 SKU_CONTEXT。
目标平台暂时未确定，不要编造无法确认的规格、材质、认证、功效或评价。
```

如果你已经知道平台和屏数，可以这样写：

```text
请使用 $sku-amazon 基于我的 SKU_CONTEXT 规划 Amazon US Listing Images 和 A+ Content。
先核对 Main Image、附图和 A+ 的不同规则，再给方向。
```

## 产品处理模式

| 模式 | 适合场景 | 产品处理方式 |
| --- | --- | --- |
| A 严格保真 | 品牌款、高客单、外观必须完全一致 | 使用真实产品抠图，AI 只生成背景、场景、光影和留白 |
| B AI 辅助商品图 | 普通 SKU、快速上新、小白用户 | 基于真实产品图做背景替换、轻度重绘或场景化生成，并做一致性质检 |
| C 概念生成 | 新品提案、方向测试、没有实物图 | 只用于概念探索，不能当作真实 SKU 成品图 |

## 不可违反的规则

1. 真实产品图是唯一产品身份来源。
2. 不编造品牌、规格、尺寸、材质、认证、功效、评价和售后承诺。
3. 材质无法确认时，只能描述“可见质感”“视觉上接近”或“真实材质待确认”。
4. 不改变真实 SKU 的颜色、结构、比例、Logo、包装文字和关键细节。
5. 竞品图只参考构图、节奏和信息结构，不复制产品、Logo、文案和品牌资产。
6. AI 图像模型不负责最终文字、Logo、参数表、认证标识和 CTA，这些建议后期排版并人工校对。

## 示例

- [墨镜详情页示例](./examples/sunglasses-detail-page.md)
- [淘宝 / 抖音 9:16 详情页示例](./examples/taobao-9-16-detail-page.md)
- [Amazon A+ 示例](./examples/amazon-a-plus-example.md)
- [安全参考竞品示例](./examples/competitor-reference-safe-use.md)

## 项目结构

```text
SKU详情页导演Skill/
├── sku-detail-page-director/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/
└── SKU详情页导演Skill.skill

skills/            公共产品核心与八个平台独立 Skill
shared/            构建时同步的公共安全、状态和质检规则
scripts/           同步、校验、素材检查与安装包构建
tests/             Skill 触发回归语料
packages/          独立 .skill 包和全平台合集
docs/              安装、排错、安全边界和 GitHub 设置说明
examples/          典型电商场景使用示例
assets/            仓库封面和展示素材
website/           可选静态网站
```

## 版本

当前开发版本：**V1.3.0-dev 多平台 Skill 拆分版**

稳定基线版本：**Lite V1.2.1**，已由 Git Tag `v1.2.1` 保留。

版本变化见 [CHANGELOG.md](./CHANGELOG.md)。

后续规划见 [ROADMAP.md](./ROADMAP.md)。

## 使用许可

本仓库的 Skill、文档、规则和示例文字可以用于学习、参考和非商业使用。

如果你引用或改编本仓库内容，请注明来源并链接回本仓库。

请不要直接搬运本仓库内容进行商业转卖。

仓库中涉及的第三方平台名称、商标、产品名和工具名，仍归各自权利人所有。

更多说明见 [NOTICE.md](./NOTICE.md) 和 [LICENSE](./LICENSE)。

## 关于作者

**秋水 Kero**，AIGC 创作者，持续分享 AI、图片和电商视觉工作流。

X（推特）：[@Isonlyonenice](https://x.com/Isonlyonenice)
