# 从“原图保真”到“身份锁定的创意重构”：KeRo-SKU-Agent 智能化研究

> 研究日期：2026-07-16
> 研究范围：WatchaAI/e-commerce 源代码与工作流；淘宝/天猫、京东、拼多多、1688、Amazon、Shopify、TikTok Shop 的一手平台资料；KeRo-SKU-Agent 的下一轮架构改造。
> 证据标准：只采用项目源代码、平台官方文档、官方商家学院、官方设计规范和官方协议。平台没有公开给出结论时，明确标为“推断”，不把行业经验伪装成平台规则。

## 结论先行

当前问题的根源不是“保真要求太高”，而是把两个概念错误地合并了：

1. **商品身份必须真实**：镜框轮廓、镜片形状、鼻梁结构、铰链、镜腿、颜色、Logo、包装和实际包含物不能漂移。
2. **画面表现必须使用原图像素**：每一屏都把同一张墨镜抠图放进去，场景、机位、光影和叙事只能围着它打转。

第一条必须保留，第二条不应该成为全局硬规则。各平台的一手资料显示，严格程度应按素材槽位决定，而不是按整个项目“一刀切”：Amazon 和 TikTok Shop 的主图确实要求客观、真实、白底；但它们的附图、A+、视频或推广内容允许展示使用场景、不同角度、细节和故事。淘宝官方 AI 商品图服务明确把商品换背景、穿戴、模特换场景和创意生图列为能力；Shopify 直接提供 AI 背景、光线和扩图工具；京东则同时要求“真实”和“自然使用场景的沉浸感”。这意味着正确路线是：**把真实 SKU 作为身份约束和证据源，而不是把原图当作所有画面的唯一像素来源。** [淘宝官方 AI 商品图制作规范](https://developer.alibaba.com/docs/doc.htm?articleId=122245&docType=1&treeId=253)；[淘宝绘蛙生图 API](https://developer.alibaba.com/docs/api.htm?apiId=69826)；[京东 Jelly 产品图像规范](https://jdrdl.jd.com/Design-image.html)；[Amazon Product Images](https://sellercentral.amazon.com/seller-forums/discussions/t/04805fc7-b165-472c-9339-725d1c2b52dc)；[Shopify Magic 媒体生成](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/shopify-magic/media-generation)；[TikTok Shop Product Listing Policy](https://seller-us.tiktok.com/university/essay?knowledge_id=3196690250417921)

建议把 KeRo-SKU-Agent 升级为六层系统：

1. 事实层：记录什么是真的、证据在哪里、什么不能说。
2. 身份锁定层：把“不可变商品特征”和“可自由重构的表现变量”分开。
3. 创意策略层：从人群、购买障碍、平台槽位和产品记忆点生成创意命题，而不是直接写 Prompt。
4. 方向提案层：先给 3 个真正不同的视觉世界，让用户选择；不能只换颜色和背景。
5. 生产层：按槽位和工具能力选择原图、像素保留合成、受控参考图编辑或概念探索。
6. 质检层：分别检查事实、身份、视觉逻辑、参考图边界、平台规则和 AI 瑕疵。

最终目标不是“放松保真”，而是把保真从一句笼统的禁止令变成可执行的身份合同，同时把场景、光线、构图、镜头、材质环境、人物、叙事、动效和图形系统释放出来。

## 一、研究方法与事实边界

### 1.1 本地仓库检查

`docs/` 下原先没有 `research` 目录或研究报告命名约定，因此本报告保存于 `docs/research/creative-commerce-visual-systems.md`。

当前 KeRo-SKU-Agent 已经具备有价值的基础：

- `SKU_CONTEXT V1` 分开记录已确认事实、谨慎推断、禁止主张和缺失证据。
- 现有模式 A/B/C 已区分真实图严格保真、受控背景/光影编辑和概念生成。
- `per-unit-production.md` 已包含逐槽位 Prompt、Negative Prompt、镜头矩阵、排版、身份检查和通用 Prompt 拦截。
- 平台 Skill 已区分主图、附图、SKU 图、详情模块、A+、PDP Section 等不同素材槽位。

所以问题不是“完全没有创意机制”，而是：

- 模式 B 的启用门槛偏保守，工具能力未知时几乎总会落回模式 A。
- 方向提案缺少结构化“创意命题”，模型容易生成“高级背景 + 柔光 + 留白”的同质方案。
- `SKU_CONTEXT` 只记录允许/禁止编辑，没有记录每个身份特征的优先级、容差、视角可信度和每个槽位的创意自由度。
- 质检能拦截商品漂移，却没有判断三个方向是否真的不同、视觉隐喻是否与产品有关、参考图是否只被“换皮复刻”。

以上是对当前仓库文件的分析，不是平台事实。

### 1.2 外部来源限制

- WatchaAI/e-commerce 的公开树在研究时只有 4 次提交，文件包括 README、一个 Markdown Skill、4 个 reference 文件、一个 `openai.yaml` 和一个打包 `.skill`；未发现脚本、自动化工作流、测试目录或性能评估文件。因此它是一个**提示词工作流包**，不是有可验证自主执行能力的代码型 Agent。[仓库首页](https://github.com/WatchaAI/e-commerce/tree/76abddb8988f87c0995f1ae79af273717c266ec8)
- 该仓库没有公开 `LICENSE` 文件。可以学习其工作流机制，但不应直接复制大段文字、模板或打包内容。
- 拼多多公开网页没有提供一套可完整引用的“视觉创意设计指南”。本报告只把其官方“如实描述”保障当作事实；关于拼多多适合怎样的视觉结构，均标为推断，并要求上线时以商家后台当前规则为准。[拼多多消费者保障](https://www.yangkeduo.com/home/customer)

## 二、WatchaAI/e-commerce 深度检查

### 2.1 实际文件结构

在固定提交 `76abddb8988f87c0995f1ae79af273717c266ec8` 上，核心文件是：

- [`README.md`](https://github.com/WatchaAI/e-commerce/blob/76abddb8988f87c0995f1ae79af273717c266ec8/README.md)
- [`SKILL.md`](https://github.com/WatchaAI/e-commerce/blob/76abddb8988f87c0995f1ae79af273717c266ec8/%E5%95%86%E5%93%81%E8%AF%A6%E6%83%85%E9%A1%B5skill/ecommerce-detail-page-workflow/SKILL.md)
- [`references/workflow.md`](https://github.com/WatchaAI/e-commerce/blob/76abddb8988f87c0995f1ae79af273717c266ec8/%E5%95%86%E5%93%81%E8%AF%A6%E6%83%85%E9%A1%B5skill/ecommerce-detail-page-workflow/references/workflow.md)
- [`references/connected_reference_count_workflow.md`](https://github.com/WatchaAI/e-commerce/blob/76abddb8988f87c0995f1ae79af273717c266ec8/%E5%95%86%E5%93%81%E8%AF%A6%E6%83%85%E9%A1%B5skill/ecommerce-detail-page-workflow/references/connected_reference_count_workflow.md)
- [`references/output_templates.md`](https://github.com/WatchaAI/e-commerce/blob/76abddb8988f87c0995f1ae79af273717c266ec8/%E5%95%86%E5%93%81%E8%AF%A6%E6%83%85%E9%A1%B5skill/ecommerce-detail-page-workflow/references/output_templates.md)
- [`references/category_notes.md`](https://github.com/WatchaAI/e-commerce/blob/76abddb8988f87c0995f1ae79af273717c266ec8/%E5%95%86%E5%93%81%E8%AF%A6%E6%83%85%E9%A1%B5skill/ecommerce-detail-page-workflow/references/category_notes.md)
- [`agents/openai.yaml`](https://github.com/WatchaAI/e-commerce/blob/76abddb8988f87c0995f1ae79af273717c266ec8/%E5%95%86%E5%93%81%E8%AF%A6%E6%83%85%E9%A1%B5skill/ecommerce-detail-page-workflow/agents/openai.yaml)

### 2.2 值得复用的机制

以下是源文件可直接验证的事实：

1. **渐进式素材收集**：先产品图，再产品信息，最后参考详情页；不一次性向用户索要长清单。这个节奏能降低用户负担，也便于每一步发现问题。[SKILL.md](https://github.com/WatchaAI/e-commerce/blob/76abddb8988f87c0995f1ae79af273717c266ec8/%E5%95%86%E5%93%81%E8%AF%A6%E6%83%85%E9%A1%B5skill/ecommerce-detail-page-workflow/SKILL.md)
2. **产品图先诊断再生产**：检查模糊、曝光、色偏、反光、透视、材质、Logo 和缺失角度，并生成逐图精修提示词。[workflow.md](https://github.com/WatchaAI/e-commerce/blob/76abddb8988f87c0995f1ae79af273717c266ec8/%E5%95%86%E5%93%81%E8%AF%A6%E6%83%85%E9%A1%B5skill/ecommerce-detail-page-workflow/references/workflow.md)
3. **多视图一致性闸门**：在进入产品信息前，要求所有上传图都有精修结果，并检查颜色、材质、光线、比例、结构、Logo 和包装文字一致性。
4. **按参考长图实际模块数确定 N**：不是机械固定 10 屏。参考页有 6 个模块就规划 6 页；边界不清时先做语义分段。[connected workflow](https://github.com/WatchaAI/e-commerce/blob/76abddb8988f87c0995f1ae79af273717c266ec8/%E5%95%86%E5%93%81%E8%AF%A6%E6%83%85%E9%A1%B5skill/ecommerce-detail-page-workflow/references/connected_reference_count_workflow.md)
5. **先策划、再提取 Prompt、最后生成**：完整方案不会直接进入生图；先提取页面专属 Prompt、统一风格 Prompt 和统一负面 Prompt，再逐页生成。
6. **参考图角色分离**：产品多视图负责身份，参考详情页负责色调、节奏、排版和模块数；默认最终生图不再把参考长图直接传给模型，降低直接复刻参考商品的风险。
7. **类别适配**：眼镜/珠宝/包强调轮廓、材质、五金、佩戴、细节和包装；3C 强调结构、功能、界面和参数；不同品类不是同一套十屏话术。[category notes](https://github.com/WatchaAI/e-commerce/blob/76abddb8988f87c0995f1ae79af273717c266ec8/%E5%95%86%E5%93%81%E8%AF%A6%E6%83%85%E9%A1%B5skill/ecommerce-detail-page-workflow/references/category_notes.md)
8. **可从后续阶段继续**：若用户已经有策划 Markdown 或视觉设计文件，工作流不会强制从头重跑。

这些机制适合吸收到 KeRo-SKU-Agent，特别是“渐进式收集”“参考图语义分段”“计划—提取—生产分离”和“断点续作”。

### 2.3 不应照搬的部分

以下结论是基于源文件的推断，已与事实分开：

1. **推断：白底三视图被提升为唯一产品依据，容易造成表现僵化。** Connected workflow 明确把“产品白底三视图”设为最终身份锁，并要求每页都连接它。这样有利于一致性，但如果生图工具把参考图当作构图模板，结果容易反复出现同一角度、同一产品占比和同一贴图感。
2. **推断：参考图模块数不应高于平台槽位。** Watcha 以参考图可见模块数决定 N；如果参考来自另一个平台，可能把别的平台长图节奏带进 Amazon A+、Shopify Section 或 TikTok Shop PDP。KeRo 应采用“用户要求 > 目标平台槽位 > 参考节奏 > 通用默认”的优先级。
3. **推断：统一负面 Prompt 过长，且大量使用全局禁止词，会压制可用创意。** 身份保护更适合变成结构化约束和局部编辑范围，而不是只依赖一串“不要改变”。Negative Prompt 不能证明输出没有漂移。
4. **推断：该工作流缺少方向选择闸门。** 它在收齐素材后直接生成 N 页完整方案；没有要求先向用户展示 3 个创意命题并确认，这会让 Agent 看似自动化，实际可能在错误方向上产出大量页面。
5. **推断：缺少平台级槽位与发布状态。** 公开文件默认 9:16，适合某些长页生产，但不是 Amazon A+、Shopify 响应式 Section、淘宝主图或 TikTok Shop 方图的通用格式。
6. **事实限制：没有脚本和测试。** 因此不能从仓库内容证明“自动多图一致性”“参考屏数识别”或“生成质量”在任何模型上可靠；这些是工作流要求，不是经代码验证的能力。

### 2.4 建议吸收方式

| Watcha 机制 | KeRo 应保留 | KeRo 应修正 |
|---|---|---|
| 逐步收素材 | 先产品证据，再商业信息，再参考/平台 | 已有资料时跳过，不重复询问 |
| 白底精修与三视图 | 作为证据板和身份源之一 | 不作为所有画面的唯一构图源 |
| 参考图模块数 | 用于分析信息节奏 | 平台槽位和用户目标优先 |
| 统一风格 Prompt | 形成跨屏视觉 Token | 变成结构化 Token，不只是一段形容词 |
| 逐页 Prompt 提取 | 保留计划和生产隔离 | 生产前增加方向批准与槽位合法性检查 |
| 最终不传参考长图 | 适用于高抄袭风险或模型易复制时 | 允许把合法场景/姿势参考用于受控编辑，但必须声明角色与权利 |

## 三、各平台一手资料：哪里必须真实，哪里可以创意

## 3.1 淘宝 / 天猫

### 官方事实

- 淘宝发布端区分 1:1 与 3:4 主图槽位；淘宝与天猫使用相同的相关图片上传接口。新版详情更推荐维护 1:1 主图，但这不是“所有详情图都必须白底”的规则。[商品接口调整通知](https://developer.alibaba.com/support/announcementDetail.htm?id=25721)
- 淘宝官方精选 AI 商品图服务要求服务商支持平铺图上身、模特换脸/换背景和商品换背景，并要求 AI 结果经过人工精修和图片检测后才能交付。[官方精选 AI 商品图制作规范](https://developer.alibaba.com/docs/doc.htm?articleId=122245&docType=1&treeId=253)
- 淘宝“绘蛙”相关 API 暴露了参考图相似度、商品原图、商品蒙版、人物蒙版、文生背景/上传背景、自动匹配人物位置等字段；`image_type=10` 明确表示眼镜，任务类型包含万物穿戴、创意生图、裂变套图和商品换背景。[绘蛙 API](https://developer.alibaba.com/docs/api.htm?apiId=69826)
- 淘宝新版图文编辑器以一份内容同时服务电脑端和手机端，并支持图片热区模块。这意味着详情内容应按模块和跨端阅读设计，不应默认输出一张不可适配的固定长图。[图文编辑器升级说明](https://developer.alibaba.com/docs/doc.htm?articleId=121094&docType=1&treeId=796)

### 可执行推断

- 淘宝/天猫的“创意自由”应主要放在轮播附图、详情模块、品牌叙事和穿戴/场景图；主图、SKU 属性图、包装文字和高品牌敏感图仍应使用高保真方式。
- 对墨镜，可以合法地把原图转化为佩戴图、室内外场景图、光影纯色背景或创意静物，但必须保留同一镜框、镜片、Logo、颜色和比例，并经过人工身份复核。官方 AI 服务的存在证明“变场景/穿戴”是平台生态认可的能力，但不等于每个类目、每个槽位都自动允许 AI 重绘。
- 天猫应比普通淘宝多一层品牌视觉系统：固定品牌色、字体、留白、材料语言和叙事语气；但品牌故事、奖项和技术仍需证据。

## 3.2 京东

### 官方事实

- 京东 Jelly 设计规范把商品图原则定义为“清晰、真实、自然”：图片应反映产品真实观感，同时贴近自然使用过程，营造沉浸感。[产品图像规范](https://jdrdl.jd.com/Design-image.html)
- 规范建议优先正视图，部分商品使用斜视图展示更多细节；主体约占画面 60%，利用留白提升格调；背景优先低饱和单色，创意背景不要复杂到干扰商品。[产品图像规范](https://jdrdl.jd.com/Design-image.html)
- 京东的总设计原则要求聚焦实际问题、简洁统一、兼顾受众差异，并用视觉锚定品牌调性。[设计原则](https://jdrdl.jd.com/Design.html)
- 运营色彩规范要求色彩服务品牌性、识别性和包容度；渐变应柔和、沉浸、有品质，避免大量撞色。[运营头图规范](https://jdrdl.jd.com/Design-Operation-head.html)

### 可执行推断

- 京东的创意不是“越炫越好”，而是让真实商品在更有秩序的空间、材质和光线中显得可信、专业。适合：低饱和背景、明确的结构近景、自然佩戴、克制渐变、参数/兼容/包装证据。避免把科技蓝光、芯片、实验室当作没有证据的性能替代品。
- 对墨镜，首图可采用简洁低饱和几何台面；附图可用真实自然佩戴、镜腿/铰链微距和尺寸关系；“电影海报式奇幻景观”不符合这套设计语言，除非作为非发布概念方向。

## 3.3 拼多多

### 官方事实

- 拼多多官方消费者保障写明，商家承诺实际商品或服务与发布描述相符；违背如实描述承诺，消费者可以售后并主张赔付。[拼多多消费者保障](https://www.yangkeduo.com/home/customer)
- 拼多多用户协议说明商品名称、价格、数量、型号、规格、尺寸、瑕疵、限制等信息由商家编辑上传，平台通过协议和规则要求描述准确、完整、可靠、有效、没有错误和误导。[拼多多用户服务协议](https://www.yangkeduo.com/pdd_user_services_agreement.pdf)

### 资料缺口

本次没有找到一套可公开、稳定访问并完整描述主图/轮播/SKU 图/详情图视觉创意的官方商家文档。因此，不能把第三方文章常见的具体尺寸、红黄促销风格或“平台偏爱大字低价图”写成官方规则。执行时必须读取商家后台当前类目要求。

### 可执行推断

- 拼多多创意的第一任务应是消除“图里是什么、最低价买到什么、数量是多少、是否含配件”的疑虑。创意可以来自产品规模感、使用场景、套装拆解、交付内容和细节证据，不应依赖虚假倒计时、夸张价格锚或把完整套装代表低价配件 SKU。
- 对墨镜，可做佩戴场景、脸型/穿搭氛围、镜片颜色展示和包装清单；但 SKU 图必须对应具体镜框颜色、镜片颜色、数量和包含物。

## 3.4 1688

### 官方事实

- 1688 官方服务条款把平台定义为 B2B 在线信息发布与交易平台，允许用户以文字、图片发布和推广产品，但要求产品信息真实并与实际销售内容一致；商家可自行决定促销推广方式，只要符合法律和平台要求。[1688 服务条款](https://terms.alicdn.com/legal-agreement/terms/suit_bu1_b2b/suit_bu1_b2b201703271338_74297.html)
- 条款强调采购者确认品名、价格、数量、型号、规格和尺寸等重要事项，说明 B2B 页面视觉必须帮助采购判断，而不只是营造情绪。[1688 服务条款](https://terms.alicdn.com/legal-agreement/terms/suit_bu1_b2b/suit_bu1_b2b201703271338_74297.html)
- 同属阿里 B2B 体系的 Alibaba.com 官方卖家资料强调高质量产品图片和视频用于第一印象、专业能力与信任；店铺可用照片、视频、文字和数字图形建立品牌，并应提供充分信息。[图片与视频课程](https://seller.alibaba.com/learningcenter/content/detail/PXJTD6WM.htm)；[B2B Storefront 指南](https://seller.alibaba.com/storefront)
- Alibaba.com 官方商品发布规则要求图片真实反映产品、清晰完整，并允许详情展示实物全图、细节图、包装图、效果图、功能、使用说明和配件。[商品信息发布规范](https://activities.alibaba.com/alibaba/productposting/terms-of-use/zh_cn.php)

### 可执行推断

- 1688 的“创意质感”应表现工厂和供货能力：产品特写、材料/工艺、可定制区域、打样流程、QC、包装、装箱、MOQ/阶梯价、交期和物流。宏观氛围图只能做开场，不能代替采购信息。
- 对墨镜，优质方向不是连续 8 屏时尚大片，而是“品牌款式感 + 镜框细节 + 可选颜色/SKU + 包装 + Logo 定制位置 + 样品/OEM 流程 + QC/产能证据”。如果没有工厂、检测或产能资料，相关模块必须留空或标记待证。

## 3.5 Amazon

### 官方事实

- Amazon 官方卖家提示要求 MAIN 图只展示实际售卖商品、白底、商品填充画面；所有图片必须准确代表商品。附图则可以展示使用中/环境中、不同角度和不同功能。[Amazon Product Images](https://sellercentral.amazon.com/seller-forums/discussions/t/04805fc7-b165-472c-9339-725d1c2b52dc)
- Amazon A+ 可以组合文字、图片、品牌 Logo、比较表和技术规格；Premium A+ 还支持视频、热点、轮播和 Q&A，Brand Story 用于品牌背景与产品线叙事。[A+ Content Design Guide](https://sell.amazon.com/blog/a-plus-content-design-guide)
- Amazon 官方建议构建故事、展示使用场景、使用专业高分辨率图片，并避免重复同一张图或使用与商品无关的泛生活方式图；A+ Content Manager 也提供生成式 AI 新图能力。[A+ Best Practices](https://sellercentral.amazon.com/seller-forums/discussions/t/969ad286-38ec-4c44-8851-14dcdf7c99c2)
- A+ 图文应平衡，复杂文字不要烘焙进图片，以免移动端缩放后不可读。[A+ Content Design Guide](https://sell.amazon.com/blog/a-plus-content-design-guide)

### 可执行推断

- Amazon 必须把主图和创意层彻底拆开：MAIN 使用严格证据图；Secondary Images 用不同角度、佩戴、细节、尺度和场景；A+ 用模块节奏、品牌故事、规格、比较表、热点和视频建立质感。
- 对墨镜，创意不应发生在 MAIN，而应发生在佩戴生活方式图、镜片/镜腿细节、尺寸示意、包装、Brand Story 和 A+ 模块。比较表只能比较自家真实 ASIN 和可验证字段。

## 3.6 Shopify

### 官方事实

- Shopify 产品媒体支持图片、视频、3D 模型，并认为 3D/视频可以帮助顾客理解功能和尺寸、提高对质量的信心。[Product media](https://help.shopify.com/en/manual/products/product-media)
- Shopify 官方摄影指南强调高质量照片、白平衡、照明、造型、后期和多角度；白底适合突出商品，但不是唯一媒体形式。[Taking product photographs](https://help.shopify.com/en/manual/products/product-media/product-photography)
- Shopify Magic 可以移除或生成背景、修改光线与其他画面因素，并可扩展画布背景；官方示例包括“温暖灯光的厨房”“阳光公园”“混凝土背景的专业广告摄影”。[Media generation](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/shopify-magic/media-generation)
- Shopify Product Media 支持图片、视频、3D/AR；高质量媒体和不同媒体类型用于帮助顾客理解商品。[Product media types](https://help.shopify.com/en/manual/products/product-media/product-media-types)
- Shopify 官方生活方式摄影指南把真实、情绪、动作和故事视为重要手段；商品在真实情境中能帮助顾客想象其如何进入生活。[Lifestyle photography](https://www.shopify.com/blog/lifestyle-photography)

### 可执行推断

- Shopify 没有 marketplace 主图的统一硬模板，创意自由度最高，但必须接受响应式、性能、可访问性、Variant 映射和真实 Add to Cart 的约束。
- 对墨镜，可以使用电影感 Hero、编辑式佩戴、Lookbook、视频、3D/AR、细节热点和滚动叙事；但每个 Variant 应映射真实媒体，关键规格和购买信息应保留为 HTML，而不是全部烘焙进长图。

## 3.7 TikTok Shop

### 官方事实

- TikTok Shop 美国 Product Listing Policy 要求主图展示商品正面物理视图、纯白背景、客观直接，禁止用数字渲染替代商品；附图可以展示使用场景、变化款、造型场景、近景和尺寸对比，但必须准确代表顾客实际收到的商品。[Product Listing Policy](https://seller-us.tiktok.com/university/essay?knowledge_id=3196690250417921)
- Seller Center 的添加商品指南同时提供 `AI Optimize` 改背景，并建议至少用不同角度和关键特征；这说明“后台 AI 改背景能力”和“主图不得数字渲染”必须按槽位与政策解释，不能简单推导为所有图片都能 AI 重绘。[How to Add Products](https://seller-us.tiktok.com/university/essay?knowledge_id=6581713858676522)
- TikTok Shop 推广内容指南要求内容准确、相关、原创；建议实时演示、多个角度、制作过程、打包过程、设计灵感和品牌故事。商品在形状、尺寸、图案、数量、Logo 或印花上不匹配会构成不一致。[Promotional Content Best Practices](https://seller-us.tiktok.com/university/essay?knowledge_id=5769635937191681)
- 商品页质量指南建议至少 5 张图，并用多角度、纹理/细节、视频和场景解释商品。[PDP & Listing Quality](https://seller-us.tiktok.com/university/essay?knowledge_id=481891871868714)

### 可执行推断

- TikTok Shop 应拆成两条生产线：PDP 资产遵守严格的实体商品和白底主图规则；短视频、直播和 Shoppable Content 以原创演示、人物、动作、制作/包装和故事建立创意。
- 对墨镜，PDP 主图用真实正面；附图做侧面、佩戴、近景、尺寸与包装；推广内容可做换装、户外光线变化、第一视角试戴和设计故事，但必须始终展示同款镜框、镜片、图案、Logo 和数量。

## 四、跨平台共同规律：创意不是改变产品，而是改变表达系统

平台资料共同支持以下结构：

| 层面 | 必须锁定 | 可创意重构 | 条件性变量 |
|---|---|---|---|
| 商品身份 | 类别、轮廓、结构、比例、颜色、Logo、标签、变体、包含物 | 无 | 只有真实可选 Variant 才能改变 |
| 场景 | 不得暗示不存在的功能或交付物 | 室内外空间、台面、建筑、自然环境、人物、道具 | 场景必须符合使用逻辑 |
| 光线 | 不得把颜色或透光表现改成另一 SKU | 光源方向、软硬、色温、轮廓光、阴影节奏、反射环境 | 不能掩盖真实颜色、Logo 和结构 |
| 构图 | 产品必须可识别，不能被道具遮挡 | 中心/偏置、对称/不对称、留白、层次、分屏、连续长页 | 受平台安全区和槽位比例约束 |
| 镜头 | 未提供的隐藏结构不能被当作事实 | 景别、机位、焦段感、运动、微距、俯拍、斜视、佩戴视角 | 新角度必须有足够多视图证据 |
| 材质表现 | 产品自身材质不能被虚构 | 背景材质、台面、织物、玻璃、石材、雾、纸张、金属环境 | 产品表面高光可以优化但不能改变材质结论 |
| 叙事 | 卖点和结果必须有证据 | 开场悬念、使用过程、细节发现、身份表达、购买收口 | 功效类叙事需证明 |
| 图形系统 | Logo/认证不可由模型伪造 | 网格、线条、色块、编号、图标、动效、信息卡 | 文字和真实 Logo 后期排版 |

### 4.1 十个真正产生视觉质感的维度

Agent 不应只输出“高级、干净、有质感”。每个方向至少要对以下维度做明确选择：

1. **创意命题**：这套画面要让顾客产生什么新理解？
2. **产品角色**：证据物、时尚符号、解决方案、工艺对象、礼物还是生活伙伴？
3. **空间世界**：棚拍、建筑、自然、家居、工厂、抽象舞台或人物生活。
4. **镜头语法**：英雄正面、斜侧、微距、佩戴半身、第一视角、动态跟拍等。
5. **光线戏剧**：硬日光、柔窗光、轮廓光、低调聚光、反射光、渐变影等。
6. **材质对话**：环境材料如何衬托商品，而不是把商品材质编造掉。
7. **构图节奏**：产品占比、留白、信息密度、左右动势、近远景变化。
8. **图形语言**：字体、线条、色块、网格、编号、热点和交互方式。
9. **叙事弧线**：识别 → 欲望 → 使用 → 证据 → 规格 → 信任 → 行动。
10. **平台行为**：搜索点击、滑动轮播、A+ 浏览、PDP 交互、短视频停留或询盘。

若三个方向只改变第 5 项色温或第 3 项背景，它们不是三个方向，只是三个配色版本。

## 五、建议的新架构：六层智能化系统

## 5.1 事实层（Fact Layer）

保留现有 `facts.verified / cautious_inferences / prohibited_claims / missing_evidence`，并新增：

- `claim_evidence_map`：每条文案绑定图片、文档、用户陈述或官方来源。
- `variant_delivery_map`：每个 SKU 的颜色、数量、包装、价格、包含物和对应图。
- `view_confidence`：正面/侧面/背面/细节是否有真实证据，防止生成未见角度。
- `platform_rule_snapshot`：链接、核对日期、类目/站点和后台截图。

输出不是“先写好看文案”，而是可生产与不可生产的事实地图。

## 5.2 身份锁定层（Identity Lock Layer）

把目前笼统的 `fidelity_requirements` 拆成四类：

```yaml
identity_lock:
  immutable_traits:
    - trait: lens_outer_contour
      evidence: [IMG_01, IMG_03]
      priority: critical
    - trait: bridge_shape
      evidence: [IMG_01]
      priority: critical
  bounded_traits:
    - trait: lens_reflection
      allowed_change: environment reflection may change
      forbidden_change: must not imply a different lens tint or coating
  unknown_traits:
    - trait: hidden_hinge_structure
      reason: no macro or side evidence
  allowed_transformations:
    - background replacement
    - contact shadow reconstruction
    - lighting relight without color shift
    - scene and model integration
  prohibited_transformations:
    - frame silhouette redesign
    - logo relocation
    - lens color replacement
```

关键改变是：**同时写“锁什么”和“放开什么”**。只有禁止项没有自由项，模型就会保守复读原图；只有自由项没有身份锚点，模型就会生成相似款。

## 5.3 创意策略层（Creative Strategy Layer）

在任何正式 Prompt 前，先生成 `CREATIVE_BRIEF`：

```yaml
creative_brief:
  business_goal: null
  target_audience: null
  purchase_barrier: null
  desired_customer_feeling: null
  product_truth_to_dramatize: []
  visual_memory_points: []
  creative_thesis: null
  product_role: null
  scene_world: null
  visual_metaphor: null
  narrative_arc: []
  novelty_target: null
  cliches_to_avoid: []
  platform_behavior: null
```

“视觉隐喻”只能解释真实特征。例如镜框线条可以与城市建筑几何形成呼应；但没有防紫外线证据时，不能用“光盾”“阻挡紫外线粒子”的画面暗示性能。

## 5.4 方向提案层（Direction Proposal Layer）

每次默认给 3 个差异足够大的方向卡，不立即生成整页：

```yaml
direction:
  id: D1
  name: null
  one_sentence_thesis: null
  sales_task: null
  desired_emotion: null
  visual_world: null
  product_role: null
  camera_grammar: []
  lighting_grammar: []
  material_environment: []
  composition_system: null
  graphic_system: null
  narrative_arc: []
  proof_plan: []
  identity_treatment: null
  suggested_fidelity_mode: null
  suitable_slots: []
  unsuitable_slots: []
  reference_abstraction: []
  creativity_risk: null
  compliance_risk: null
```

方向通过条件：

- 任意两方向至少在创意命题、场景世界、产品角色、镜头语法、叙事弧线中有三项不同。
- 每个方向都必须引用至少两个产品专属记忆点。
- 每个方向都说明适合哪些平台槽位、不适合哪些槽位。
- 用户确认方向后才进入逐屏生产；若用户说“按你推荐的”，Agent 列出推荐理由和默认假设。

## 5.5 生产层（Production Layer）

### 建议用 F0-F3 取代模糊的全局 A/B/C

为了兼容现有模式，可保留旧字段并增加映射：旧 A → F0/F1，旧 B → F2，旧 C → F3。

| 模式 | 产品本体如何形成 | 创意空间 | 发布边界 |
|---|---|---|---|
| F0 证据原图 | 原始照片或忠实精修照片 | 裁切、曝光、白平衡、清洁 | 主图、SKU 图、包装/认证证据优先 |
| F1 像素保留合成 | 真实产品抠图不重绘；生成场景/背景/光影后合成 | 场景、构图、材质环境、道具、图形系统高度自由 | 文生图工具、严格槽位、品牌敏感商品 |
| F2 身份条件编辑/重构 | 多视图、蒙版、结构锚点约束下进行参考图编辑、穿戴或受控重构 | 新光线、新机位、新场景、人物佩戴、姿态和叙事 | 只用于平台允许槽位；必须人工身份检查 |
| F3 概念探索 | 可生成概念化产品/极端视觉 | 最大 | `direction-only`，不能直接发布为真实 SKU |

F1 是解决“原图贴上去很死板”的第一条路线：商品像素不变，但整个空间、光线、阴影、构图和图形系统可以重做。F2 是更大胆的路线：不要求最终画面保留原图像素，但要求模型把多视图身份合同带入新场景，并且通过身份质检。两者都比“每一屏硬贴同一张原图”更有创意。

### 每个槽位新增创意自由度

```yaml
creative_freedom:
  score: 0  # 0-4
  background: locked | controlled | free
  lighting: locked | controlled | free
  camera: source-view-only | evidence-bounded | free
  scene: none | realistic | editorial | conceptual
  model_or_human: prohibited | allowed-with-evidence | allowed
  props: included-items-only | contextual | free-nonmisleading
  graphics: none | post-production-only | allowed
  product_regeneration: prohibited | controlled | concept-only
```

- 0：只允许原始证据展示。
- 1：裁切、清洁、曝光和白平衡。
- 2：允许背景、接触阴影、受控光线和排版。
- 3：允许真实使用场景、人物、道具、受控新机位。
- 4：允许强概念和抽象表达，但仍需保留商品可识别度；若改变产品本体，只能 F3。

### 工具路由

- 只支持文字生图：使用 F1，生成不含商品的场景底图，再合成真实商品。
- 支持参考图编辑/蒙版：可使用 F2，明确商品蒙版、允许编辑区和禁止编辑区。
- 支持多图/结构控制：F2 可启用新机位，但只限有证据的角度和结构。
- 工具能力未知：不等于整页只能 F0；至少可做 F1 的背景与图形系统生产。
- 文本、Logo、价格、参数、认证：后期真实图层或 HTML，不依赖模型烘焙。

## 5.6 质检层（QA Layer）

### 六道闸门

1. **事实闸门**：每条参数、材质、功效、兼容、认证、价格和包含物可追溯。
2. **身份闸门**：对比轮廓、比例、关键点、颜色、Logo、标签、包装和 Variant。
3. **表现真实性闸门**：反射、阴影、人物佩戴和道具不制造错误用途、尺寸或功能印象。
4. **创意质量闸门**：方向是否有独立命题，是否与产品有关，是否只是通用“高级背景”。
5. **平台闸门**：主图、附图、SKU 图、A+、PDP Section 和推广内容没有混用。
6. **参考与权利闸门**：没有复制参考商品、Logo、文案、品牌故事或受保护人物。

### 建议状态

- `ready`：事实、身份、平台和权利均通过。
- `human-review`：F2 重构、人物、复杂反射或高风险类目需要人工确认。
- `direction-only`：F3 或缺少关键产品证据。
- `blocked`：SKU、包含物、平台规则或声明证据不足。
- `repair-required`：身份或 AI 瑕疵失败，必须返修而非继续生产。

自动像素差异、轮廓相似度或关键点比对只能作为提示，不能被描述为“保证同款”。最终发布仍需人工视觉比对。

## 六、参考图使用边界

| 参考类型 | 可提取 | 不可复制 | 最终生图是否传入 |
|---|---|---|---|
| 用户真实产品图 | 商品身份、角度、颜色、结构、Logo、包装 | 无证据的隐藏结构和材质结论 | F0/F1/F2 均可按角色使用 |
| 用户品牌资产 | 品牌色、字体、Logo、图形规范 | 不得让模型重绘 Logo/认证 | Logo 后期真实图层；规范可进入 Prompt |
| 竞品详情页 | 信息结构、节奏、镜头类型、留白、抽象色彩关系 | 竞品商品、文案、Logo、品牌故事、独特图形和一比一布局 | 默认只做分析；高复制风险时不传最终模型 |
| 风格参考图 | 光线、色调、材质环境、构图原则、摄影语言 | 原作品的具体主体与独创组合 | 权利明确且工具需要时可作为 F2 风格参考 |
| 场景/姿势参考 | 姿势、机位、场景关系 | 人物身份、服装图案、品牌、受保护形象 | 仅在授权清楚且不造成复制时使用 |
| AI 概念图 | 方向、氛围、候选构图 | 不得反向升级为真实产品证据 | 只用于方向或背景参考 |

Agent 应输出 `reference_abstraction_report`：

```yaml
reference_id: REF_01
role: competitor_layout | style | scene | pose | product_identity
rights_status: user-owned | licensed | unknown
abstracted_traits:
  - asymmetric hero composition
  - warm hard sunlight
  - large quiet negative space
excluded_traits:
  - competitor product
  - logo and copy
  - unique campaign symbol
final_generation_use: analysis-only | prompt-only | image-reference
```

## 七、墨镜示例：如何“锁定身份但不硬贴原图”

### 7.1 身份合同

假设现有图片可以确认以下内容：

- 镜片外轮廓与弧度。
- 镜框上沿和下沿关系。
- 鼻梁形状与双侧连接位置。
- 铰链和镜腿起点。
- 镜框颜色、镜片色调、Logo 位置。
- 包装盒/镜布是否属于实际交付。

这些是锁定项。可自由变化的是：

- 背景空间与环境材质。
- 日光、窗光、轮廓光、反射光和阴影图案。
- 正视、斜侧、微距、佩戴半身等有证据的镜头。
- 产品在画面中的大小、位置、层次和留白。
- 人物服装与场景，但不能遮住镜框关键结构。
- 版式、网格、线条、编号、局部动画和页面衔接。
- 镜片环境反射，但不能改变真实镜片色或暗示无证据的镀膜/防护能力。

### 7.2 三个真正不同的方向

#### D1｜光学雕塑

- 命题：把镜框轮廓当作一件可被观察的设计对象。
- 空间：半透明亚克力、磨砂玻璃、浅色几何台面。
- 镜头：英雄斜侧 + 镜腿/铰链微距 + 轮廓投影。
- 光线：硬边光和克制渐变阴影。
- 图形：细线标注、宽留白、低密度排版。
- 生产：主图 F0/F1；详情附图 F1/F2。
- 风险：不要用光谱、UV 盾等图形暗示未证实光学能力。

#### D2｜城市镜面

- 命题：镜框几何与现代城市线条形成视觉对应，表达穿搭态度。
- 空间：玻璃幕墙、石材、金属栏杆的真实城市环境。
- 镜头：人物佩戴中景、步行动作、镜片环境反射、侧面细节。
- 光线：自然硬日光，控制高光，不改变镜片色。
- 图形：编辑式杂志网格、短标题、大留白。
- 生产：PDP 主图仍 F0；场景附图/Shopify Hero/推广内容使用 F2。
- 风险：没有侧面证据时，不生成完整镜腿暴露角度。

#### D3｜旅行日光

- 命题：让商品进入真实出行时刻，突出轻松、阳光与佩戴氛围，而不是凭空宣称性能。
- 空间：暖色石墙、车窗、海边步道或咖啡馆外摆。
- 镜头：手持、佩戴、收纳取出、包装仪式。
- 光线：金色时段自然光与柔和反射。
- 图形：温暖色块、路线式节奏、短故事文案。
- 生产：淘宝/天猫轮播、Shopify、TikTok 推广适合 F2；Amazon MAIN 不适合。
- 风险：场景只能表达生活方式，不能自动推导防晒、偏光或 UV 等级。

这三套方案的区别不是背景颜色，而是商品角色、空间世界、镜头语法、光线和叙事都不同。

## 八、建议的 `SKU_CONTEXT V2` 字段

```yaml
sku_context_version: 2

product_identity:
  category: null
  product_name: null
  variants: []
  source_images: []
  reference_priority: []
  view_confidence: {}

facts:
  verified: []
  cautious_inferences: []
  prohibited_claims: []
  missing_evidence: []
  claim_evidence_map: []

identity_lock:
  immutable_traits: []
  bounded_traits: []
  unknown_traits: []
  allowed_transformations: []
  prohibited_transformations: []
  variant_delivery_map: []

creative_brief:
  business_goal: null
  target_audience: null
  purchase_barrier: null
  desired_customer_feeling: null
  product_truth_to_dramatize: []
  creative_thesis: null
  product_role: null
  visual_metaphor: null
  narrative_arc: []
  novelty_target: null
  cliches_to_avoid: []

reference_system:
  references: []
  abstraction_reports: []
  rights_risks: []

directions:
  candidates: []
  selected_direction: null
  rejected_directions: []
  approval_status: pending

production:
  fidelity_mode: null  # F0/F1/F2/F3
  creative_freedom: {}
  tool_capabilities: []
  source_and_mask_plan: []
  platform_slots: []
  generation_units: []

qa:
  fact_status: null
  identity_status: null
  creative_quality_status: null
  platform_status: null
  reference_rights_status: null
  human_review_required: false
  repair_tasks: []
```

## 九、完整的新工作流程

1. **识别任务**：平台、站点、类目、目标槽位、语言、商业目标。
2. **渐进收集证据**：先产品图与包装，再产品信息，再参考图；已有资料则直接复用。
3. **建立事实层**：已确认、推断、禁止、缺失和声明—证据映射。
4. **建立身份合同**：不可变、有限可变、未知、允许变换和禁止变换。
5. **计算槽位自由度**：每个主图/附图/SKU 图/A+/PDP Section/视频单独评分。
6. **分析参考图**：做语义分段和抽象化，不复制具体商品与品牌。
7. **建立创意 Brief**：人群、障碍、情绪、命题、商品角色、隐喻和叙事。
8. **提出 3 个方向**：确保不是换色版本；给推荐、风险和适用槽位。
9. **用户批准方向**：只问一个真正改变路线的问题。
10. **建立平台资产地图**：用户要求和平台槽位优先，参考页模块数只作节奏参考。
11. **选择 F0-F3**：按槽位和工具能力决定产品如何进入画面。
12. **逐单元生产**：画面规范 → 产品来源/蒙版 → Prompt → 后期排版 → QA。
13. **生成/合成**：先场景与商品层，再真实文字、Logo、价格、参数和 CTA。
14. **六道质检**：事实、身份、表现真实性、创意、平台、参考权利。
15. **断点续作**：保存方向、身份合同、资产状态和修复任务，下轮从当前阶段继续。
16. **学习记录**：记录用户偏好和被拒方向，但不能把一次偏好伪装成所有 SKU 的默认审美。

## 十、对当前仓库的可执行改造清单

### P0：先解决“原图硬锁”和方向同质化

1. 更新 `skills/sku-product-core/references/sku-context-schema.md` 为兼容 V1 的 V2，新增 `identity_lock`、`creative_brief`、`reference_system`、`directions` 和 `qa`。
2. 更新 `skills/sku-product-core/references/core-rules.md`：把“保真模式”从全局决定改成“按平台槽位决定”，增加 F0-F3 映射。
3. 新建 `shared/creative-direction-system.md`：定义十个创意维度、方向差异阈值、方向卡字段和通用创意词拦截。
4. 更新 `SKU详情页导演Skill/sku-detail-page-director/SKILL.md`：在平台 handoff 前生成 3 个结构化方向，并等待用户确认。

### P1：让平台 Skill 真正释放不同自由度

5. 每个平台 `platform-rules.md` 增加 `creative_opportunity_by_slot`：严格槽位、受控槽位、自由槽位、禁用表现。
6. Amazon/TikTok Shop 明确主图 F0、附图 F1/F2、A+/推广内容独立；Shopify 允许更高自由度和视频/3D；1688 把创意转向采购证据；京东增加自然沉浸和克制背景语言。
7. `shared/per-unit-production.md` 增加 `creative_thesis`、`product_role`、`creative_freedom`、`reference_abstraction`、`identity_anchors` 和 `release_gate` 字段。

### P2：建立真实可运行的生产与质检能力

8. 为 F1 增加产品抠图、场景底图、接触阴影、色彩匹配和后期合成的明确流程。
9. 为 F2 增加多视图参考、商品蒙版、允许编辑区、禁止编辑区和新角度证据检查。
10. 增加 identity landmarks：眼镜至少记录镜片外轮廓、鼻梁、铰链、镜腿起点、Logo 锚点和镜片色。
11. 增加“方向差异质检”：三个方向若只换颜色/背景，测试失败。
12. 增加“视觉隐喻质检”：隐喻若暗示未证实功效，测试失败。

### P3：测试案例

至少增加以下前向测试：

- 同一副墨镜输出三个视觉世界，身份一致但场景、光线、镜头、叙事明显不同。
- Amazon MAIN 拒绝 F2 数字重构，Secondary/A+ 允许合规生活方式与细节图。
- TikTok Shop PDP 主图拒绝数字渲染，推广短视频允许真实演示和原创故事。
- Shopify 为每个 Variant 映射真实媒体，并保留 HTML 价格/CTA。
- 缺少墨镜侧面图时，不生成暴露隐藏铰链结构的新角度。
- 竞品参考只提取节奏和构图，不复制 Logo、文案、商品和独特品牌符号。
- 拼多多完整套装图与最低价单件 SKU 不一致时阻塞。
- 1688 没有产能/QC/OEM 证据时，不生成工厂能力声明。

## 十一、最终判断

KeRo-SKU-Agent 不应该退回“随便发挥、像不像无所谓”，也不应该继续“所有屏都只能使用同一张原图墨镜”。更成熟的系统应做到：

- 原图是证据，不是审美牢笼。
- 商品身份是结构化合同，不是一串 Negative Prompt。
- 创意发生在场景、光线、构图、镜头、材质环境、人物、叙事、图形和交互中。
- 是否允许重构由“平台 + 槽位 + 工具 + 证据”共同决定。
- 严格主图保留真实商品；附图、详情、A+、Shopify Section 和推广内容逐级释放自由度。
- 先提案、再确认、后生产；先判断方向是否独特，再判断图片是否漂亮。

WatchaAI/e-commerce 最值得借鉴的是渐进式素材收集、参考图模块分析、计划与生图分离；最不应照搬的是把白底三视图变成唯一表现来源、默认 9:16 和缺少方向批准/平台槽位的统一生产。KeRo 的优势已经在事实、平台和逐单元协议上，下一轮应该补的是**身份锁定下的创意推理**，而不是继续增加更多禁止项。

## 十二、主要一手来源

### WatchaAI/e-commerce

- [仓库固定提交](https://github.com/WatchaAI/e-commerce/tree/76abddb8988f87c0995f1ae79af273717c266ec8)
- [SKILL.md](https://github.com/WatchaAI/e-commerce/blob/76abddb8988f87c0995f1ae79af273717c266ec8/%E5%95%86%E5%93%81%E8%AF%A6%E6%83%85%E9%A1%B5skill/ecommerce-detail-page-workflow/SKILL.md)
- [Workflow Checklist](https://github.com/WatchaAI/e-commerce/blob/76abddb8988f87c0995f1ae79af273717c266ec8/%E5%95%86%E5%93%81%E8%AF%A6%E6%83%85%E9%A1%B5skill/ecommerce-detail-page-workflow/references/workflow.md)
- [Connected Reference-Count Workflow](https://github.com/WatchaAI/e-commerce/blob/76abddb8988f87c0995f1ae79af273717c266ec8/%E5%95%86%E5%93%81%E8%AF%A6%E6%83%85%E9%A1%B5skill/ecommerce-detail-page-workflow/references/connected_reference_count_workflow.md)
- [Output Templates](https://github.com/WatchaAI/e-commerce/blob/76abddb8988f87c0995f1ae79af273717c266ec8/%E5%95%86%E5%93%81%E8%AF%A6%E6%83%85%E9%A1%B5skill/ecommerce-detail-page-workflow/references/output_templates.md)
- [Category Notes](https://github.com/WatchaAI/e-commerce/blob/76abddb8988f87c0995f1ae79af273717c266ec8/%E5%95%86%E5%93%81%E8%AF%A6%E6%83%85%E9%A1%B5skill/ecommerce-detail-page-workflow/references/category_notes.md)

### 淘宝 / 天猫 / 阿里

- [淘宝商品接口调整通知：1:1 与 3:4 主图](https://developer.alibaba.com/support/announcementDetail.htm?id=25721)
- [淘宝官方精选 AI 商品图制作规范](https://developer.alibaba.com/docs/doc.htm?articleId=122245&docType=1&treeId=253)
- [淘宝绘蛙生图 API](https://developer.alibaba.com/docs/api.htm?apiId=69826)
- [淘宝图文编辑器升级](https://developer.alibaba.com/docs/doc.htm?articleId=121094&docType=1&treeId=796)
- [1688 服务条款](https://terms.alicdn.com/legal-agreement/terms/suit_bu1_b2b/suit_bu1_b2b201703271338_74297.html)
- [Alibaba.com 商品发布规范](https://activities.alibaba.com/alibaba/productposting/terms-of-use/zh_cn.php)
- [Alibaba.com Seller Storefront](https://seller.alibaba.com/storefront)

### 京东

- [Jelly 产品图像规范](https://jdrdl.jd.com/Design-image.html)
- [Jelly 设计原则](https://jdrdl.jd.com/Design.html)
- [Jelly 运营头图与色彩](https://jdrdl.jd.com/Design-Operation-head.html)

### 拼多多

- [拼多多消费者保障](https://www.yangkeduo.com/home/customer)
- [拼多多用户服务协议](https://www.yangkeduo.com/pdd_user_services_agreement.pdf)

### Amazon

- [Amazon Product Images](https://sellercentral.amazon.com/seller-forums/discussions/t/04805fc7-b165-472c-9339-725d1c2b52dc)
- [Amazon A+ Content Design Guide](https://sell.amazon.com/blog/a-plus-content-design-guide)
- [Amazon A+ Content Best Practices](https://sellercentral.amazon.com/seller-forums/discussions/t/969ad286-38ec-4c44-8851-14dcdf7c99c2)
- [Amazon Product Photography](https://sell.amazon.com/blog/product-photos)

### Shopify

- [Shopify Product Media](https://help.shopify.com/en/manual/products/product-media)
- [Shopify Product Photography](https://help.shopify.com/en/manual/products/product-media/product-photography)
- [Shopify Magic Media Generation](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/shopify-magic/media-generation)
- [Shopify Product Media Types](https://help.shopify.com/en/manual/products/product-media/product-media-types)
- [Shopify Lifestyle Photography](https://www.shopify.com/blog/lifestyle-photography)

### TikTok Shop

- [TikTok Shop Product Listing Policy](https://seller-us.tiktok.com/university/essay?knowledge_id=3196690250417921)
- [TikTok Shop How to Add Products](https://seller-us.tiktok.com/university/essay?knowledge_id=6581713858676522)
- [TikTok Shop Promotional Content Best Practices](https://seller-us.tiktok.com/university/essay?knowledge_id=5769635937191681)
- [TikTok Shop Product Detail Pages & Listing Quality](https://seller-us.tiktok.com/university/essay?knowledge_id=481891871868714)
