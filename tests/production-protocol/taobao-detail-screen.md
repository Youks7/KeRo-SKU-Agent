# 淘宝逐屏生产协议回归样例

## 整页生产总控

已确认方向：搜索识别 + 结构细节。目标平台：淘宝移动端详情。处理模式：模式 A。视觉 Token：中性浅灰背景、左上柔和主光、黑色文字、统一 24 px 网格。来源只使用 `front.jpg`、`side.jpg` 和 `hinge.jpg`；不得主张材质、偏光、UV、尺寸、认证或包含物。

## 生产单元 01｜结构识别首屏

平台槽位 / 模块类型：淘宝移动端详情模块 01
销售任务：让用户识别真实黑色全框墨镜及镜框到镜腿的结构。
发布状态：human-review
本单元依赖：`front.jpg` 的正面轮廓、`side.jpg` 的镜腿形态、`hinge.jpg` 的铰链局部。
禁止主张 / 缺失证据：不得写偏光、UV、防蓝光、具体材质和尺寸。

未来画面：真实正面产品抠图位于画面中下部，右上留标题区，底部使用真实铰链局部裁切作为证据卡片。
主文案：轮廓与结构，一眼看清
副文案 / 证据文案：正面、侧面和铰链细节均来自当前真实 SKU 图片。
文案位置与安全区：主标题右上，距离边缘不少于画布短边 6%；证据文案位于底部卡片外，不覆盖产品。

产品处理模式：A
处理理由：正式商品详情首屏且产品结构必须与实物一致。
允许修改：背景、光影、自然接触阴影和排版留白。
禁止修改：镜框轮廓、镜片颜色、镜桥、铰链、镜腿、Logo 区域和产品数量。
产品来源与合成方式：AI 只生成背景；后期分别合成 `front.jpg` 抠图和 `hinge.jpg` 真实裁切。

镜头矩阵：
- 景别：产品全貌 + 局部特写。
- 视角 / 机位：正面平视；铰链局部保持来源视角。
- 产品朝向 / 状态：镜腿自然展开，与来源图一致。
- 产品占比 / 位置：主体约占画布宽度 64%，位于中下部。
- 背景 / 道具：中性浅灰摄影棚背景，无道具。
- 光线 / 阴影 / 反射：左上柔光，轻微接触阴影，不改变镜片颜色。
- 景深 / 透视：背景轻微层次，产品本体保持真实透视。
- 与前后单元的差异及衔接：首屏展示全貌；下一单元转入侧面结构，不重复正面构图。

Prompt：Generate only a neutral light-gray mobile commerce background with soft directional studio light from the upper left, a clean contact-shadow area reserved for the real front-view black full-rim sunglasses cutout in the lower center, a separate bottom detail-card area reserved for the real hinge crop, and mobile-safe negative space in the upper right. Do not generate the product. Do not generate glasses, text, logos, labels, dimensions, certification icons, packaging, accessories, people, or props.
Negative Prompt：product, sunglasses, eyeglasses, duplicate object, text, letters, numbers, logo, watermark, label, package, accessories, certification, UV, polarized, material claim, distorted geometry, colored lens shift, harsh reflection, clutter, generic black-gold e-commerce template

后期排版：
- 画布比例 / 尺寸 / 响应式裁切：按当前淘宝后台详情模块宽度导出，不预设固定 9:16；保留移动端安全裁切。
- 文字图层、字体层级、对齐和行数：文字全部使用可编辑图层；主标题最多两行，左对齐。
- 产品、文字、标识和 CTA 的安全区：产品与文字不重叠，不加入假按钮或平台标识。
- 色彩、对比度、边缘、阴影和导出要求：检查抠图边缘、黑位层次和 sRGB 导出。

产品一致性质检：
1. 对比 `front.jpg` 检查镜框、镜桥、镜片颜色和产品数量。
2. 对比 `hinge.jpg` 检查铰链局部没有重绘或镜像错误。
3. 检查没有额外眼镜盒、配件、Logo、标签或虚构文字。
4. 检查主副文案未引入材质、尺寸、功效和认证声明。
5. 当前状态保持 `human-review`，完成抠图边缘和颜色人工复核后才能改为 `ready`。

通用 Prompt 拦截自检：
1. Prompt 引用了黑色全框轮廓和真实铰链裁切两个产品专属细节，不是任意商品模板。
2. 没有只写“高级背景 + 柔光 + 留白”。
3. 未混入缺失功效、尺寸、材质或平台禁用元素。
4. 镜头与下一侧面模块不同。
5. 结果：通过，无需重写。
