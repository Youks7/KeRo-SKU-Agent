---
name: sku-jd
description: "Create JD-native product image and detail-page plans with verified parameters, model compatibility, package contents, installation conditions, warranty responsibility, and service boundaries. Use when users mention 京东、JD、京东主图、京东参数详情、兼容性、包装清单、质保、安装说明或专业商品页。"
---

# 京东 SKU 详情页

把商品视觉、结构化参数、兼容性、包装和服务承诺连接到同一证据链。

## 读取规则

读取 [`references/common-safety.md`](references/common-safety.md) 和 [`references/platform-rules.md`](references/platform-rules.md)。类目参数和资质以京东商家后台与规则中心当前要求为准。

## 工作流

1. 继承 `SKU_CONTEXT`，补充型号、规格、兼容性、包装、安装、质保和售后证据。
2. 建立参数—证据矩阵，未知数字保持为空。
3. 区分主图、附图、参数模块、兼容性、安装使用和服务模块。
4. 根据购买疑虑生成专业证明型方向，不用科技光效替代真实性能证据。
5. 用户确认后逐模块输出画面、结构化文案、Prompt、处理模式和校验点。
6. 检查图片、参数、包装清单和服务承诺的一致性。

## 输出

输出 `参数—证据矩阵`、`兼容性表`、`包装清单`、`素材模块计划`、`服务边界` 和 `发布质检`。

