<h1 align="center">先保護真實 SKU，再做不套模板的電商詳情頁</h1>

<p align="center"><strong>KeRo SKU Skill</strong></p>

<p align="center">真實產品保真 · 三階段決策 · 防同質化生產 · 逐屏商業圖</p>

<p align="center">以真實產品為唯一身分來源，確認方向後才進入正式生成。</p>

<p align="center">
  <a href="./README.md">简体中文</a> ·
  <a href="./README_EN.md">English</a> ·
  繁體中文<br>
  <a href="./SKU详情页导演Skill/SKU详情页导演Skill.skill">下載 Skill</a> ·
  <a href="./SKU详情页导演Skill/sku-detail-page-director/references/SKU详情页导演Skill_Lite_V1.2.1_防同质化生产优化版.md">查看完整規則（簡體中文）</a> ·
  <a href="https://x.com/Isonlyonenice">X：@Isonlyonenice</a>
</p>

---

## 這是什麼

KeRo SKU Skill 是一個面向電商營運、設計師和 AIGC 創作者的 Codex Skill。

上傳真實產品圖後，它會先辨識可確認的事實與產品保真風險，再提出 3 個明顯不同的詳情頁方向。只有使用者確認方向後，才會繼續輸出逐屏方案、生圖 Prompt 和商業圖。

適用於淘寶、天貓、京東、拼多多、抖音商城、小紅書、Amazon、Shopify、TikTok Shop 及其他電商平台。

## 三個階段完成一套詳情頁

| 階段 | AI 負責 | 你只需要 |
| --- | --- | --- |
| 01 產品分析 | 辨識產品、事實邊界、風險和視覺機會 | 上傳真實產品圖 |
| 02 方向提案 | 提供 A / B / C 三種詳情頁方向 | 選擇一個或混合方向 |
| 03 商業圖生產 | 輸出逐屏方案、Prompt 和質檢要求 | 確認屏數、比例和交付方式 |

```text
真實產品圖
   ↓
產品深度分析
   ↓
選擇 A / B / C 方向
   ↓
逐屏方案與商業圖
```

## 快速開始

### 1. 安裝

下載 [`SKU详情页导演Skill.skill`](./SKU详情页导演Skill/SKU详情页导演Skill.skill) 並匯入 Codex。

也可以把 `SKU详情页导演Skill/sku-detail-page-director/` 整個目錄複製到 Codex 的 skills 目錄。

### 2. 上傳產品圖

盡量提供正面、側面、45°、細節和包裝圖。重要的 Logo、結構、鏡片、介面或包裝文字建議另外補拍。

### 3. 傳送啟動指令

```text
請使用 $sku-detail-page-director 分析我上傳的產品圖。

先執行階段一：產品深度分析。
在我確認方向前，不要輸出正式生圖 Prompt。
不能編造圖片和資料中無法確認的規格、材質、認證、功效或評價。
```

## 標準生產流程

### 階段一：產品深度分析

```text
這是我的產品圖，請先做階段一：產品深度分析。

目標平台：淘寶 / 抖音商城通用
輸出語言：繁體中文
預計屏數：8 屏
核心賣點：暫不確定，請根據圖片謹慎判斷

不能編造圖片裡看不出來的規格、材質、認證、功效和使用者評價。
```

階段一會輸出：

- 可以確認的事實與禁止編造的資訊
- 建議的產品處理模式及風險
- 產品氣質、購買機會和同質化掃描
- 3 個來自產品本身的視覺記憶點
- 下一步需要確認的唯一決策

### 階段二：選擇方向

```text
繼續，進入階段二，給我 3 個詳情頁方向。
```

AI 會提供 A / B / C 三個方向。直接回覆：

```text
選 A。
```

也可以混合：

```text
A + C 混合，以 A 的轉換邏輯為主，加入 C 的高級質感。
```

### 階段三：逐屏生產

```text
依照確認方向製作 8 屏。
每一屏單獨輸出，一共輸出 8 張圖片，比例 9:16。
生成前先提供目前屏幕的銷售任務、構圖、Prompt 和產品一致性質檢點。
```

正式商用文字、Logo、參數和 CTA 建議在後製階段排版。需要快速預覽時，可以讓 AI 生成帶文字版本，但必須人工校對。

## 三種產品處理模式

| 模式 | 適合情境 | 產品處理方式 |
| --- | --- | --- |
| A 嚴格保真 | 品牌款、高單價、外觀必須完全一致 | 使用真實產品去背，AI 只生成背景和光影 |
| B AI 輔助商品圖 | 一般 SKU、快速上架 | 基於真實產品圖做情境化或輕度重繪，並執行一致性質檢 |
| C 概念生成 | 新品提案、方向測試 | 只用於概念探索，不可當作真實 SKU 成品圖 |

## 不可違反的規則

1. 真實產品圖是唯一產品身分來源。
2. 競品圖只參考構圖、節奏和資訊結構，不複製產品、Logo、文字和品牌資產。
3. 不編造品牌、規格、尺寸、材質、認證、功效、評價和售後承諾。
4. 材質無法確認時，只能描述「可見質感」「視覺上接近」或「真實材質待確認」。
5. 不改變真實 SKU 的顏色、結構、比例、Logo 和關鍵細節。
6. 每一屏必須有不同的銷售任務、構圖和產品專屬視覺記憶點。

---

## 進階 SOP

下面內容預設收合，需要時點擊標題展開。

<details>
<summary><strong>完整資料準備清單</strong></summary>

一般專案不需要一次填完。先提供產品圖和已知資訊，缺少的內容可以在流程中補充。

1. 產品名稱
2. 目標平台
3. 需要製作的內容：詳情頁、主圖、SKU 圖、副圖或 A+ 頁面
4. 圖片尺寸或比例
5. 正面、側面、45°、細節、包裝、SKU 和真人使用圖
6. 主推 SKU
7. 全部顏色、款式、規格和組合
8. 最想突出的 3 個核心賣點
9. 尺寸、重量、材質、規格、顏色和包裝清單
10. 檢測報告、認證、專利、授權或質檢報告
11. 目標使用者
12. 主要使用情境
13. 想要的視覺風格
14. 參考圖或競品連結
15. 不能寫或不能出現的內容
16. Logo、品牌色、字體和包裝原始檔
17. 交付時間

</details>

<details>
<summary><strong>分析錯誤時如何修正</strong></summary>

不需要重新開始整個專案，直接補充或修正錯誤資訊。

```text
補充一下：
平台改成小紅書 + 抖音商城。
核心賣點是便攜和高顏值，不主打低價。
材質不能寫，因為目前沒有資料。
請依照這些資訊修正階段一，然後繼續提供 3 個方向。
```

產品類別辨識錯誤時：

```text
這裡修正一下：這不是廚房用品，而是寵物飲水器。
材質和容量目前無法確認。
請依照修正後的類別重新執行階段一。
```

</details>

<details>
<summary><strong>如何安全參考競品詳情頁</strong></summary>

```text
我上傳了真實產品圖和競品參考圖。

產品圖是我的真實產品，必須以它為準。
競品圖只參考畫面風格、構圖節奏和資訊結構，不能照抄。
不要生成競品裡的產品、Logo、文字或品牌資產。

先做階段一產品分析，再進入方向提案。
```

加入自訂主題時：

```text
只參考競品頁面的結構和節奏，不要照抄。
我的詳情頁以釣魚為核心使用情境，畫面元素簡約，真實產品必須保持一致。
```

</details>

<details>
<summary><strong>競品 Prompt 提取與產品遷移</strong></summary>

第一輪，提取競品結構：

```text
分析我上傳的 10 張競品詳情頁圖片。
依序提取每張圖的銷售任務、構圖、場景、光線、道具、文字安全區和視覺節奏，
輸出 10 個對應的背景或場景 Prompt。

不要複製競品產品、Logo、文字和品牌資產。
```

第二輪，上傳自己的真實產品：

```text
現在上傳的是我的真實產品圖，請把它作為唯一產品身分來源。
套用前面提取的結構，同時保持產品顏色、結構、比例、Logo 和關鍵細節一致。
每張圖生成前先執行產品一致性檢查。
```

Amazon：

```text
依照已確認的 Prompt 製作 Amazon 商品圖或 A+ 頁面素材。
請根據每個模組的用途選擇適合比例，不要把所有圖片都預設成 9:16。
```

</details>

<details>
<summary><strong>國內電商與 Amazon SKU 資料草稿</strong></summary>

國內電商：

```text
請根據產品多角度圖整理國內電商 SKU 資料草稿。
本輪只執行第一階段，不進入方向提案，不輸出分屏方案和生圖 Prompt。

請輸出：產品名稱、目標受眾、賣點描述、可見材質質感、使用方式和中文類目路徑。
不能編造無法確認的硬性事實。
```

Amazon：

```text
Please create a draft SKU information sheet from the uploaded multi-angle product images.
Complete Stage 1 only. Do not create directions, module plans, or image prompts yet.

Output: Product Name, Target Audience, Selling Points, Visible Material or Finish, Usage, and Amazon Category Path.
Do not invent unverified material, dimensions, weight, certification, functions, package contents, brand, or model information.
```

</details>

<details>
<summary><strong>常用圖片處理指令</strong></summary>

#### 1:1 主圖產品替換

```text
保持圖 1 的場景、構圖、光線和留白不變，
把其中的產品替換為圖 2 至圖 11 中的真實產品。
保持每個 SKU 的顏色、結構、Logo 和比例準確，分別輸出 1:1 主圖。
```

#### 白底商品圖

```text
把產品圖統一處理成商業棚拍純白背景。
保留產品真實結構和顏色，清理雜亂反光，
同時保留呈現真實材質和光學深度所需的受控高光與接觸陰影。
```

#### 中文詳情頁翻譯成英文

```text
保持產品、場景和版式結構不變，提取全部中文文案並翻譯成自然英文。
先輸出中英對照和排版建議，再生成英文預覽圖。
最終文字需要人工校對。
```

#### 3:4 多場景主圖

```text
圖 1 至圖 4 是同一產品的真實多角度圖。
設計 6 張 3:4 生活方式商品圖。
改變機位、構圖、人物服裝和場景，但保持產品身分、顏色和結構一致。
```

#### 修改鏡片顏色

```text
把圖 1 中的鏡片顏色調整為圖 2 的鏡片顏色。
只修改鏡片顏色和受控光學反射，不改變鏡框、鏡腿、Logo、結構和比例。
鏡片應保持真實光學深度，不要變成平面色塊或發光塑膠。
```

#### 五視圖擺放

```text
圖 1 是五視圖擺放模板。
使用圖 2 至圖 11 的真實產品圖，生成正面、側面、45°、背面和細節視圖。
不要編造未提供角度的隱藏結構；缺少的視角需要明確標記。
```

#### 墨鏡質感增強

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
<summary><strong>最終商用質檢清單</strong></summary>

1. 產品顏色是否與真實圖一致
2. 產品結構、比例和 SKU 是否改變
3. Logo、包裝文字和關鍵細節是否準確
4. 是否新增不存在的配件、認證、功效或功能
5. 是否把競品產品或相似款當成真實產品
6. 鏡片、反光和材質是否符合真實物理表現
7. 每一屏是否有獨立銷售任務和不同構圖
8. 每個 Prompt 是否包含產品專屬細節
9. 文字是否經過人工校對和後期排版
10. 目前圖片適合正式商用，還是只能作為方向參考

</details>

## 專案結構

```text
SKU详情页导演Skill/
├── sku-detail-page-director/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/
│       └── SKU详情页导演Skill_Lite_V1.2.1_防同质化生产优化版.md
└── SKU详情页导演Skill.skill
```

目前版本：**Lite V1.2.1 防同質化生產最佳化版**

---

## 關於我

**秋水 Kero**，AIGC 創作者，喜歡研究新工具，也喜歡分享實用又有趣的 AI 工作流程。

X（推特）：[@Isonlyonenice](https://x.com/Isonlyonenice)
