# 淘宝逐屏生产协议回归样例

## 整页生产总控

已确认方向：城市光学陈列 + 结构细节。目标平台：淘宝移动端详情。处理模式：F1。视觉 Token：冷灰建筑光影、烟灰透明亚克力层、左上狭长窗光、黑色文字、统一 24 px 网格；场景用克制的斜向明暗切割承接镜框轮廓，不生成商品本体。来源只使用 `front.jpg`、`side.jpg` 和 `hinge.jpg`；不得主张材质、偏光、UV、尺寸、认证或包含物。

## 生产单元 01｜结构识别首屏

平台槽位 / 模块类型：淘宝移动端详情模块 01
销售任务：让用户识别真实黑色全框墨镜及镜框到镜腿的结构。
发布状态：human-review
本单元依赖：`front.jpg` 的正面轮廓、`side.jpg` 的镜腿形态、`hinge.jpg` 的铰链局部。
禁止主张 / 缺失证据：不得写偏光、UV、防蓝光、具体材质和尺寸。

创意命题：把真实镜框轮廓与铰链细节组织成清晰的结构识别节奏。
槽位创意自由度：2——允许创意背景、光影、真实局部证据和排版，不重绘商品。
身份锚点：镜片外轮廓、鼻梁、铰链、镜腿起点和镜片色调。
参考抽象：只吸收建筑阴影、半透明层次、几何留白和细线证据卡；不复制竞品商品、Logo、文案或一比一构图。
发布闸门：真实抠图、局部证据和颜色人工复核通过后才能 `ready`。

未来画面：真实正面产品抠图位于画面中下部，跨在一条斜向窗光与烟灰透明亚克力台座上；右上留标题区，底部使用真实铰链局部裁切作为证据卡片。场景先生成空的产品位、接触面和阴影接收区，商品及真实投影后期合成。
主文案：轮廓与结构，一眼看清
副文案 / 证据文案：正面、侧面和铰链细节均来自当前真实 SKU 图片。
文案位置与安全区：主标题右上，距离边缘不少于画布短边 6%；证据文案位于底部卡片外，不覆盖产品。

产品处理模式：F1
处理理由：正式商品详情首屏且产品结构必须与实物一致。
生成工具能力：只生成背景，不使用参考图重绘产品
允许修改：背景、光影、自然接触阴影和排版留白。
禁止修改：镜框轮廓、镜片颜色、镜桥、铰链、镜腿、Logo 区域和产品数量。
产品来源与合成方式：AI 只生成背景；后期分别合成 `front.jpg` 抠图和 `hinge.jpg` 真实裁切。

镜头矩阵：
- 景别：产品全貌 + 局部特写。
- 视角 / 机位：正面平视；铰链局部保持来源视角。
- 产品朝向 / 状态：镜腿自然展开，与来源图一致。
- 产品占比 / 位置：主体约占画布宽度 64%，位于中下部。
- 背景 / 道具：冷灰建筑墙面、烟灰透明亚克力台座和一条克制的斜向窗光；道具不得暗示不存在的功能或尺度。
- 光线 / 阴影 / 反射：环境光方向匹配来源图；后期根据真实抠图落点建立短而柔的接触影、台座反射和边缘溢色，不改变镜片颜色或真实高光结构。
- 景深 / 透视：墙面与台座有清晰空间层次；消失线、台面角度和抠图底边保持一致，产品本体保持真实透视。
- 与前后单元的差异及衔接：首屏展示全貌；下一单元转入侧面结构，不重复正面构图。

Prompt：Generate only a cool-gray architectural mobile-commerce set with a restrained diagonal window-light band from the upper left, a smoke-gray translucent acrylic plinth, an empty PRODUCT_CUTOUT_ZONE in the lower center sized from the source cutout bounding box, a physically plausible contact-shadow receiver aligned to the plinth plane, a separate empty DETAIL_CROP_ZONE at the bottom, and mobile-safe negative space in the upper right. Preserve editable depth layers and a neutral environment-color reference for later color matching. Keep both zones empty and transparent-ready for later compositing. Do not generate any product or product-specific feature.
Negative Prompt：product, sunglasses, eyeglasses, duplicate object, text, letters, numbers, logo, watermark, label, package, accessories, certification, UV, polarized, material claim, distorted geometry, colored lens shift, harsh reflection, clutter, generic black-gold e-commerce template

后期排版：
- 画布比例 / 尺寸 / 响应式裁切：按当前淘宝后台详情模块宽度导出，不预设固定 9:16；保留移动端安全裁切。
- 文字图层、字体层级、对齐和行数：文字全部使用可编辑图层；主标题最多两行，左对齐。
- 产品、文字、标识和 CTA 的安全区：产品与文字不重叠，不加入假按钮或平台标识。
- 色彩、对比度、边缘、阴影和导出要求：先做环境色匹配，再清理抠图边缘白边；按台座平面重建接触影，添加低强度环境边缘溢色并保留真实高光；分别检查 100%、50% 和移动端缩略图，最后以 sRGB 导出。

产品一致性质检：
1. 对比 `front.jpg` 检查镜框、镜桥、镜片颜色和产品数量。
2. 对比 `hinge.jpg` 检查铰链局部没有重绘或镜像错误。
3. 检查没有额外眼镜盒、配件、Logo、标签或虚构文字。
4. 检查主副文案未引入材质、尺寸、功效和认证声明。
5. 当前状态保持 `human-review`，完成抠图边缘和颜色人工复核后才能改为 `ready`。
6. 检查环境色匹配、接触影方向与软硬、边缘溢色和台座透视；任一项使商品显得悬浮、变色或贴纸化时标记 `repair-required`。

通用 Prompt 拦截自检：
1. 背景 Prompt 没有描述或生成产品；黑色全框轮廓和真实铰链两个专属细节已在来源、合成和质检字段锁定。
2. 没有只写“高级背景 + 柔光 + 留白”。
3. 未混入缺失功效、尺寸、材质或平台禁用元素。
4. 镜头与下一侧面模块不同。
5. 结果：通过，无需重写。
