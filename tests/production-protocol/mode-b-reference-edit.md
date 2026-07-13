# 模式 B 参考图编辑冲突回归样例

## 整页生产总控

目标：验证模式 B 保留来源图中已有 Logo、标签和包装文字，不再被通用 Negative Prompt 反向删除。

## 生产单元 02｜真实包装场景化

平台槽位 / 模块类型：允许参考图编辑的详情模块
销售任务：展示用户提供的真实包装与产品关系，不新增包装信息。
发布状态：human-review
本单元依赖：`product-packaging.jpg`；已确认现有 Logo 位置、标签版式和包装正面文字区域。
禁止主张 / 缺失证据：不得新增认证、奖项、功效、规格或包装内容。

未来画面：保留来源图中的产品和包装，在不遮挡既有文字的前提下替换为中性使用场景。
主文案：后期可编辑图层，当前不生成。
副文案 / 证据文案：后期只使用商家核对过的字段。
文案位置与安全区：位于包装文字区域之外。

产品处理模式：B
处理理由：目标工具支持参考图编辑，且用户允许只替换背景。
生成工具能力：支持参考图编辑与局部遮罩；支持 Negative Prompt
允许修改：背景、环境光和接触阴影。
禁止修改：产品、包装结构、现有 Logo、现有标签、现有包装文字、颜色和数量。
产品来源与合成方式：把 `product-packaging.jpg` 作为唯一身份参考，只遮罩背景区域。

镜头矩阵：
- 景别：产品与包装中景。
- 视角 / 机位：保持来源图机位。
- 产品朝向 / 状态：保持来源图。
- 产品占比 / 位置：保持来源图主体边界。
- 背景 / 道具：只替换遮罩内背景，不新增交付物。
- 光线 / 阴影 / 反射：匹配来源图主光方向。
- 景深 / 透视：不改变来源图透视。
- 与前后单元的差异及衔接：本单元负责包装证据，不重复产品全貌。

Prompt：Use product-packaging.jpg as the unique identity reference and edit only its masked background. Preserve the exact existing product, package structure, colors, quantity, Logo placement, label layout, and all existing packaging text pixels without redrawing or replacing them. Add a restrained neutral usage background and matching contact shadow outside the protected product-and-package mask. Do not invent any new claim, certification, icon, accessory, package, or text.
Negative Prompt：new logo, altered logo, missing logo, replaced label, corrupted label, misspelled existing packaging text, new packaging text, changed package structure, changed product color, extra product, extra accessory, invented certification, invented claim

后期排版：
- 画布比例 / 尺寸 / 响应式裁切：按目标平台当前详情模块规则。
- 文字图层、字体层级、对齐和行数：新文案全部后期排版，不覆盖原包装文字。
- 产品、文字、标识和 CTA 的安全区：保护产品与包装遮罩。
- 色彩、对比度、边缘、阴影和导出要求：人工对比来源图的颜色、边缘和文字像素。

产品一致性质检：
1. 对比来源图检查现有 Logo 没有移动、替换或消失。
2. 检查标签与包装文字没有重绘、乱码或拼写变化。
3. 检查产品、包装、数量和颜色保持一致。
4. 检查没有新增认证、功效、赠品或配件。
5. 完成人工像素复核前保持 `human-review`。

通用 Prompt 拦截自检：
1. Prompt 明确绑定唯一来源图和受保护区域。
2. Negative Prompt 禁止的是 Logo、标签和文字的变化，而不是把这些已有元素本身列为负面词。
3. 产品、Logo和包装文字保留要求没有互相冲突。
4. 结果：通过。
