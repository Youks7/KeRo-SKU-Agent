<h1 align="center">先保护真实 SKU，再做不套模板的电商详情页</h1>

<p align="center"><strong>KeRo SKU Skill</strong></p>

<p align="center">真实产品保真 · 三阶段决策 · 防同质化生产 · 逐屏商业图</p>

<p align="center">以真实产品为唯一身份来源，确认方向后才进入正式生成。</p>

<p align="center">
  简体中文 ·
  <a href="./README_EN.md">English</a> ·
  <a href="./README_ZH-TW.md">繁體中文</a><br>
  <a href="./SKU详情页导演Skill/SKU详情页导演Skill.skill">下载 Skill</a> ·
  <a href="./SKU详情页导演Skill/sku-detail-page-director/references/SKU详情页导演Skill_Lite_V1.2.1_防同质化生产优化版.md">查看完整规则</a> ·
  <a href="https://x.com/Isonlyonenice"> 作者：@Isonlyonenice</a>
</p>

---

## 这是什么

KeRo SKU Skill 是一个面向电商运营、设计师和 AIGC 创作者的 Codex Skill。

上传真实产品图后，它会先判断产品事实与保真风险，再提供 3 个明显不同的详情页方向。只有用户确认方向后，才继续输出分屏方案、生图 Prompt 和商业图。

适用于淘宝、天猫、京东、拼多多、抖音商城、小红书、Amazon、Shopify 和 TikTok Shop。

## 三步完成一套详情页

| 阶段 | AI 负责 | 你只需要 |
| --- | --- | --- |
| 01 产品分析 | 识别产品、事实边界、风险和视觉机会 | 上传真实产品图 |
| 02 方向提案 | 给出 A / B / C 三种详情页方向 | 选择一个或混合方向 |
| 03 商业图生产 | 输出逐屏方案、Prompt 和质检要求 | 确认屏数、比例和交付方式 |

```text
真实产品图
   ↓
产品深度分析
   ↓
A / B / C 三方向选择
   ↓
逐屏方案与商业图
```

## 快速开始

### 1. 安装

下载 [`SKU详情页导演Skill.skill`](./SKU详情页导演Skill/SKU详情页导演Skill.skill) 并导入 Codex。

也可以把 `SKU详情页导演Skill/sku-detail-page-director/` 整个目录复制到 Codex 的 skills 目录。

### 2. 上传产品图

尽量提供正面、侧面、45°、细节和包装图。重要的 Logo、结构、镜片、接口或包装文字建议单独补拍。

### 3. 发送启动指令

```text
请使用 $sku-detail-page-director 分析我上传的产品图。

先执行阶段一：产品深度分析。
在我确认方向前，不要输出正式生图 Prompt。
不能编造图片和资料中无法确认的规格、材质、认证、功效或评价。
```

## 标准生产流程

### 阶段一：产品深度分析

```text
这是我的产品图，请先做阶段一：产品深度分析。

目标平台：淘宝 / 抖音商城通用
输出语言：中文
预计屏数：8 屏
核心卖点：暂不确定，请根据图片谨慎判断

不能编造图片里看不出来的规格、材质、认证、功效和用户评价。
```

阶段一会输出：

- 可以确认的事实与不能编造的信息
- 推荐的产品处理模式及风险
- 产品气质、购买机会和同质化扫描
- 3 个来自产品本身的视觉记忆点
- 下一步需要确认的唯一决策

### 阶段二：选择方向

```text
继续，进入阶段二，给我 3 个详情页方向。
```

AI 会提供 A / B / C 三个方向。直接回复：

```text
选 A。
```

也可以混合：

```text
A + C 混合，以 A 的转化逻辑为主，加入 C 的高级质感。
```

### 阶段三：逐屏生产

```text
按确认方向制作 8 屏。
每一屏单独输出，一共输出 8 张图片，比例 9:16。
生成前先给出当前屏的销售任务、构图、Prompt 和产品一致性质检点。
```

正式商用文字、Logo、参数和 CTA 建议后期排版。需要快速预览时，可以让 AI 生成带文字版本，但必须人工校对。

## 三种产品处理模式

| 模式 | 适合场景 | 产品处理方式 |
| --- | --- | --- |
| A 严格保真 | 品牌款、高客单、外观必须完全一致 | 使用真实产品抠图，AI 只生成背景和光影 |
| B AI 辅助商品图 | 普通 SKU、快速上新 | 基于真实产品图做场景化或轻度重绘，并执行一致性质检 |
| C 概念生成 | 新品提案、方向测试 | 只用于概念探索，不可当作真实 SKU 成品图 |

## 不可违反的规则

1. 真实产品图是唯一产品身份来源。
2. 竞品图只参考构图、节奏和信息结构，不复制产品、Logo、文字和品牌资产。
3. 不编造品牌、规格、尺寸、材质、认证、功效、评价和售后承诺。
4. 材质无法确认时，只能描述“可见质感”“视觉上接近”或“真实材质待确认”。
5. 不改变真实 SKU 的颜色、结构、比例、Logo 和关键细节。
6. 每屏必须有不同的销售任务、构图和产品专属视觉记忆点。

---

## 进阶 SOP

下面的内容默认折叠。需要时点击标题展开。

<details>
<summary><strong>完整资料准备清单</strong></summary>

普通项目不需要一次填完。先提供产品图和已知信息，缺失项可以在流程中补充。

1. 产品名称
2. 目标平台
3. 需要制作的内容：详情页、主图、SKU 图、副图或 A+ 页面
4. 图片尺寸或比例
5. 正面、侧面、45°、细节、包装、SKU、真人使用图
6. 主推 SKU
7. 全部颜色、款式、规格和组合装
8. 最想突出的 3 个核心卖点
9. 尺寸、重量、材质、规格、颜色和包装清单
10. 检测报告、认证、专利、授权或质检报告
11. 目标用户
12. 主要使用场景
13. 想要的视觉风格
14. 参考图或竞品链接
15. 不能写或不能出现的内容
16. Logo、品牌色、字体和包装源文件
17. 交付时间

</details>

<details>
<summary><strong>分析错误时怎么纠正</strong></summary>

不用重新开始整个项目，直接补充或纠正错误信息。

```text
补充一下：
平台改成小红书 + 抖音商城。
核心卖点是便携和高颜值，不主打低价。
材质不能写，因为暂时没有资料。
请基于这些信息修正阶段一，并继续给我 3 个方向。
```

产品类目识别错误时：

```text
这里纠正一下：这个不是厨房用品，而是宠物饮水器。
材质和容量暂时不能确认。
请基于这个修正，重新做阶段一分析。
```

</details>

<details>
<summary><strong>如何安全参考竞品详情页</strong></summary>

```text
我上传了真实产品图和竞品参考图。

产品图是我的真实产品，必须以它为准。
竞品图只参考画面风格、构图节奏和信息结构，不能照抄。
不要生成竞品里的产品、Logo、文字或品牌资产。

先做阶段一产品分析，再进入方向提案。
```

如果希望加入自己的主题：

```text
请参考竞品页面的结构和节奏，但不要照抄。
我的详情页以钓鱼为核心使用场景，画面元素简约，真实产品必须保持一致。
```

</details>

<details>
<summary><strong>简化版竞品 Prompt 提取与产品迁移</strong></summary>

第一轮，提取竞品页面：

```text
分析我上传的 10 张竞品详情页图片。
按顺序提取每张图的销售任务、构图、场景、光线、道具、文字安全区和视觉节奏，
输出 10 个对应的背景或场景 Prompt。

不要复制竞品产品、Logo、文字和品牌资产。
```

第二轮，上传自己的真实产品：

```text
现在上传的是我的真实产品图，请把它作为唯一产品身份来源。
按前面提取的结构生成新方案，同时保持产品颜色、结构、比例、Logo 和关键细节一致。
每张图生成前先做产品一致性检查。
```

国内电商：

```text
我是淘宝 / 天猫卖家，请按确认后的 10 个 Prompt 逐张制作商品详情图，比例 9:16。
```

Amazon：

```text
我是 Amazon 卖家，请按确认后的 10 个 Prompt 逐张制作商品图或 A+ 页面素材。
请根据模块用途选择合适比例，不要把所有图片默认做成 9:16。
```

</details>

<details>
<summary><strong>国内电商与 Amazon SKU 资料草案</strong></summary>

国内电商：

```text
请基于产品多角度图，整理国内电商 SKU 资料草案。

本轮只执行第一阶段，不进入方向提案，不输出分屏方案和生图 Prompt。

请输出：产品名称、目标受众、卖点描述、可见材质质感、使用方式和中文类目路径。
不能编造无法确认的硬事实，未确认功能不得写成产品功能。
```

Amazon：

```text
Please create a draft SKU information sheet from the uploaded multi-angle product images.

Only complete Stage 1. Do not create a page direction, module plan, or image-generation prompt yet.

Output: Product Name, Target Audience, Selling Points, Visible Material or Finish, Usage, and Amazon Category Path.

Do not invent unverified material, dimensions, weight, certification, function, packaging content, brand, or model information.
```

</details>

<details>
<summary><strong>常用图片处理指令</strong></summary>

#### 1:1 主图产品替换

```text
保持图 1 的场景、构图、光线和留白不变，
把其中的产品替换为图 2 至图 11 中的真实产品。
保持每个 SKU 的颜色、结构、Logo 和比例准确，分别输出 1:1 主图。
```

#### 白底商品图

```text
把产品图统一处理成商业棚拍纯白背景。
保留产品真实结构和颜色，清理杂乱反光，
同时保留表现真实材质和光学深度所需的受控高光与接触阴影。
```

#### 中文详情页转英文

```text
保持产品、场景和版式结构不变，提取全部中文文案并翻译为自然英文。
先输出中英对照和排版建议，再生成英文预览图。
最终文字需要人工校对。
```

#### 3:4 多场景主图

```text
图 1 至图 4 是同一产品的真实多角度图。
设计 6 张 3:4 生活方式商品图。
改变机位、构图、人物着装和场景，但保持产品身份、颜色和结构一致。
```

#### 修改镜片颜色

```text
把图 1 中的镜片颜色调整为图 2 的镜片颜色。
只修改镜片颜色和受控光学反射，不改变镜框、镜腿、Logo、结构和比例。
镜片应保持真实光学深度，不要变成平面色块或发光塑料。
```

#### 五视图摆放

```text
图 1 是五视图摆放模板。
使用图 2 至图 11 的真实产品图，生成正面、侧面、45°、背面和细节视图。
不要编造未提供角度的隐藏结构；缺失视角需要明确标记。
```

#### 墨镜质感增强

```text
Use the uploaded sunglasses as the strict product reference.
Preserve the exact frame, temples, lenses, bridge, hinges, logo, colors, coating direction, details, and proportions.

Improve only the commercial rendering quality: crisp industrial edges, controlled satin highlights,
realistic optical lens depth, clean reflections, a white-to-light-gray studio background,
and a soft natural contact shadow.

Do not redesign, reshape, recolor, replace, or stylize the product.
```

</details>

<details>
<summary><strong>最终商用质检清单</strong></summary>

1. 产品颜色是否与真实图一致
2. 产品结构、比例和 SKU 是否改变
3. Logo、包装文字和关键细节是否准确
4. 是否添加了不存在的配件、认证、功效或功能
5. 是否把竞品产品或相似款当成真实产品
6. 镜片、反光和材质是否真实
7. 每屏是否有独立销售任务和不同构图
8. 每个 Prompt 是否包含产品专属细节
9. 文字是否经过人工校对和后期排版
10. 当前图片适合正式商用，还是只能作为方向参考

</details>

## 项目结构

```text
SKU详情页导演Skill/
├── sku-detail-page-director/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/
│       └── SKU详情页导演Skill_Lite_V1.2.1_防同质化生产优化版.md
└── SKU详情页导演Skill.skill
```

当前版本：**Lite V1.2.1 防同质化生产优化版**

---

## 关于我

**秋水 Kero**，AIGC 创作者，喜欢折腾，也喜欢体验新鲜事物。

X（推特）：[@Isonlyonenice](https://x.com/Isonlyonenice)

持续分享 AI、图片与各种有趣的新鲜玩法。
