# 墨镜 F2 身份条件重构回归样例

## 整页生产总控

目标：验证详情页允许新机位与创意光影，同时用多视图身份合同锁定同一副真实墨镜。

## 生产单元 03｜城市佩戴侧视

平台槽位 / 模块类型：Shopify Gallery / 淘宝允许场景化的详情模块
销售任务：展示真实佩戴关系与侧面结构。
发布状态：human-review
本单元依赖：`front.jpg`、`side.jpg`、`hinge.jpg`；已确认正面轮廓、鼻梁、铰链、镜腿起点、Logo 位置和镜片色调。
禁止主张 / 缺失证据：不得写偏光、UV、防蓝光、具体材质或尺寸；没有完整隐藏结构证据。

创意命题：镜框几何与城市建筑线条形成穿搭呼应。
槽位创意自由度：3——允许真实佩戴场景、人物、受控新机位与新光线，不允许改变商品身份。
身份锚点：镜片外轮廓、鼻梁、铰链、镜腿起点、Logo 位置、镜片色调。
参考抽象：只借用城市玻璃、石材、自然硬日光与杂志网格；不复制参考人物、商品、Logo、文案或独特活动符号。
发布闸门：F2 输出必须逐项比对三张来源图并完成人工审核；失败时返修或降级 F1。

未来画面：人物在真实城市步道中侧向行走，墨镜成为清晰焦点，环境反射不改变镜片真实色调。
主文案：后期真实文字图层。
副文案 / 证据文案：只描述可见轮廓与佩戴造型，不写功能。
文案位置与安全区：画面左侧留白，不覆盖眼镜和人物眼周。

产品处理模式：F2
处理理由：目标槽位允许场景化，工具支持多图参考、蒙版与身份条件编辑。
生成工具能力：多图参考 / 局部蒙版 / Negative Prompt
允许修改：人物、服装、城市背景、机位、自然光线与环境反射。
禁止修改：镜片外轮廓、鼻梁、铰链、镜腿起点、Logo 位置、镜片色调和产品数量。
产品来源与合成方式：以三张真实来源图建立身份合同，保护眼镜区域，输出后人工比对。

镜头矩阵：
- 景别：人物肩部侧面中近景。
- 视角 / 机位：有 `side.jpg` 支持的三分之二侧视。
- 产品朝向 / 状态：正常佩戴。
- 产品占比 / 位置：眼镜区域清晰可检查。
- 背景 / 道具：城市玻璃和石材，不增加交付物。
- 光线 / 阴影 / 反射：自然硬日光，镜片反射受控。
- 景深 / 透视：背景轻度虚化，眼镜结构清楚。
- 与前后单元的差异及衔接：从静物英雄图转入人物使用关系。

Prompt：Use front.jpg, side.jpg, and hinge.jpg together as the identity contract for the same real SKU; preserve the verified lens outline, bridge geometry, hinge, temple starting point, Logo placement, frame proportions, and lens tint while reconstructing only an evidence-supported three-quarter side wearing view in a real urban glass-and-stone setting with natural hard daylight. Keep the eyewear clearly inspectable, do not invent hidden geometry, and reserve clean copy space outside the product.
Negative Prompt：different eyewear design, changed lens shape, changed bridge, invented hinge, moved or redrawn Logo, altered lens tint, duplicate glasses, extra accessory, UV claim, polarized claim, material claim, text, watermark

后期排版：
- 画布比例 / 尺寸 / 响应式裁切：按目标槽位和移动端安全区导出。
- 文字图层、字体层级、对齐和行数：全部后期可编辑。
- 产品、文字、标识和 CTA 的安全区：不覆盖眼镜、眼周和 Logo。
- 色彩、对比度、边缘、阴影和导出要求：人工检查镜片色调、反射和边缘。

产品一致性质检：
1. 对比 `front.jpg` 检查镜片外轮廓和鼻梁。
2. 对比 `side.jpg` 检查镜腿起点与允许机位。
3. 对比 `hinge.jpg` 检查铰链，不接受虚构结构。
4. 检查 Logo 位置和镜片色调没有变化。
5. 人工复核通过前保持 `human-review`。

通用 Prompt 拦截自检：
1. 方向由城市几何与真实镜框记忆点共同形成，不是通用高级背景。
2. 使用三个来源视图和六个身份锚点。
3. 新机位受到侧面证据边界约束。
4. 未引入偏光、UV、防蓝光、材质或尺寸声明。
5. 结果：通过。
