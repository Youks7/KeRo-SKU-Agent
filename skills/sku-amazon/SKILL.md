---
name: sku-amazon
description: "Create Amazon marketplace-specific main image, secondary image, video brief, A+ Content, Premium A+, Brand Story, comparison chart, and localization plans from verified real-SKU materials. Use when users mention Amazon、ASIN、Amazon listing images、A+ Content、Premium A+、Brand Story、Brand Registry 或 Amazon 商品页优化。"
---

# Amazon SKU 页面

把 Main Image、secondary images、A+ 和 Brand Story 作为不同资产系统处理，并适配具体站点。

## 读取规则

读取 [`references/common-safety.md`](references/common-safety.md) 和 [`references/platform-rules.md`](references/platform-rules.md)。发布前核对目标站点、类目和 Seller Central 当前规则。

## 工作流

1. 继承 `SKU_CONTEXT`，确认站点、语言、类目、ASIN 状态、Brand Registry 和可用模块。
2. 区分 Main Image、secondary images、video brief、A+、Premium A+ 和 Brand Story。
3. 主图默认使用真实产品和严格保真；场景、功能信息和比较内容放入允许的附图或模块。
4. 根据主要购买疑虑生成二至三个方向，并让图片、bullet 和 A+ 使用同一事实证据。
5. 用户确认后逐资产输出目标、构图、文案层、Prompt、alt text 方向和 QA。
6. 检查语言、单位、比较、环保、兼容性、功效和认证声明。

## 输出

输出 `站点与资格检查`、`Listing Image Map`、`A+ Module Map`、`Brand Story`、`比较表`、`本地化风险` 和 `实验假设`。

