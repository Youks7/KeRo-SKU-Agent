---
name: sku-amazon
description: "Create Amazon marketplace-specific main image, secondary image, video brief, A+ Content, Premium A+, Brand Story, comparison chart, and localization plans from verified real-SKU materials. Use when users mention Amazon、ASIN、Amazon listing images、A+ Content、Premium A+、Brand Story、Brand Registry 或 Amazon 商品页优化。"
---

# Amazon SKU 页面

把 Main Image、secondary images、A+ 和 Brand Story 作为不同资产系统处理，并适配具体站点。

## 读取规则

开始时完整读取 [`references/common-safety.md`](references/common-safety.md)、[`references/creative-direction-system.md`](references/creative-direction-system.md) 和 [`references/platform-rules.md`](references/platform-rules.md)。只有用户确认方向并进入正式生产时，才完整读取 [`references/per-unit-production.md`](references/per-unit-production.md)。发布前核对目标站点、类目和 Seller Central 当前规则。

## 工作流

1. 继承 `SKU_CONTEXT`；没有上下文时先使用 `$sku-product-core`，未安装时执行最小事实与保真检查，再确认站点、语言、类目、ASIN 状态、Brand Registry 和可用模块。
2. 若有已批准的 `REFERENCE_MIGRATION_CONTEXT`，读取当前平台迁移条目并重排到 Amazon 合法槽位；Amazon Main Image、A+ 和 Brand Story 规则覆盖来源页面比例、模块数和叠字方式。
3. 区分 Main Image、secondary images、video brief、A+、Premium A+ 和 Brand Story。
4. Main Image 使用 F0；场景、细节和故事放入允许使用 F1/F2 的 Secondary、A+ 或 Brand Story。
5. 建立或复用 `CREATIVE_CONTEXT`，根据主要购买疑虑生成三个差异化方向，并让图片、bullet 和 A+ 使用同一事实证据。
6. 用户确认后，按槽位创意自由度选择 F0–F3，并严格按逐屏 / 逐模块生产协议，为每张图片和每个 A+ / Brand Story 模块完整输出 Prompt、Negative Prompt、处理模式、文案位置、后期排版、镜头矩阵、alt text、产品一致性质检和通用 Prompt 拦截。
7. 检查语言、单位、比较、环保、兼容性、功效和认证声明。

## 输出

输出 `站点与资格检查`、`Listing Image Map`、`A+ Module Map`、`整页生产总控`、`逐单元完整生产记录`、`Brand Story`、`比较表`、`本地化风险` 和 `实验假设`。
