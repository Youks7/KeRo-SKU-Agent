# Shopify 平台规则与输出结构

> 规则核对日期：2026-07-12。Shopify 是可定制店铺系统，不存在一套适用于所有主题和商家的固定“详情页图片屏数”。

## 必要输入

- 销售国家、语言、币种、主题、模板和可用应用。
- 产品、variants、价格、库存、媒体和购买选项。
- 产品分类、metafields、披露、配送、退换货和售后。
- SEO、分析工具、页面速度和品牌组件要求。

## 内容模型

把事实分配到：title、description、media、category、variants、metafields、disclosures、shipping、returns、SEO 和结构化数据。相同字段只维护一个权威来源，页面组件引用它。

## PDP Sections

- Hero：商品身份、核心价值、价格、变体和真实 Add to Cart。
- Gallery：图片、视频、可选 3D 和变体媒体。
- Benefits：用户利益与证据，不把关键文字只放在图内。
- Proof：细节、材料证据、测试、评价或信任信息；没有证据则不使用。
- Details：规格、尺寸、包含物、使用和维护。
- FAQ：解决购买前疑虑。
- Shipping/Returns：真实政策和地区差异。
- CTA：真实交互组件，可追踪事件，不是图片中的假按钮。

## 媒体与变体

每个变体映射真实媒体。颜色或款式切换后，主媒体、可用性、价格和相关信息保持一致。图片提供简洁描述性 alt text；装饰图使用适当的空 alt 策略由实现层决定。

## SEO 与可访问性

关键产品信息保留为 HTML。输出 SEO title、meta description 和图片 alt text 方向，但不堆砌关键词。检查标题层级、对比度、键盘操作和移动端阅读。

## 性能与测量

定义首屏关键媒体、响应式裁切、图片尺寸、延迟加载和视频加载策略。为变体选择、媒体互动、FAQ、Add to Cart 和购买建立分析事件与假设。

## 槽位级创意机会

- 严格身份槽位：variant media、价格、库存、包含物和 Add to Cart 使用 F0 与真实数据/组件，不把交互烘焙进图片。
- 受控创意槽位：Gallery、Details、Proof 与变体场景可用 F1/F2，保持实际商品与变体映射。
- 自由创意槽位：Hero、生活方式、视频、3D/AR、品牌故事和编辑式 Section 可在身份合同内使用 F2；F3 只做方向探索。
- 视觉语言：允许杂志化、沉浸式和交互式表达，但关键文字保留 HTML，并同时设计桌面、移动裁切、性能和可访问性。

## 输出结构

```text
店铺与主题假设
Product Content Model
PDP Section Map
Media/Variant Map
Metafield Map
SEO与Alt Text
桌面/移动布局
性能预算
分析事件与实验假设
```

## 官方核对入口

- 产品详情结构：https://help.shopify.com/en/manual/products/details/product-details-page
- 产品变体：https://help.shopify.com/en/manual/products/variants/add-variants
- 媒体 Alt Text：https://help.shopify.com/en/manual/products/product-media/add-alt-text
