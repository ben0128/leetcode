# NeetCode 提交分析 — Google SWE L4 Prep

> 分析日期：2026-04-11
> 資料來源：ben0128/neetcode-submissions-6ljxjurm
> 總解題數：181 題 | 總提交數：495（Python 410, JS 85）

---

## 一、重點掙扎題目（提交次數 >= 5）

### Tier 1：嚴重卡關（8+ 次提交）

| 題目 | 提交次數 | 主題 | 分析 |
|------|----------|------|------|
| count-connected-components | **11** | Graph / Union Find | 最大弱點。嘗試了 DFS → BFS → 多次 Union Find。最終版有 path compression + union by rank，但內化程度不夠 |
| three-integer-sum | **9** | Two Pointers | JS 3 次 + PY 6 次。卡在 duplicate-skipping 邏輯 |
| is-palindrome | **9** | Two Pointers | 最終版手動檢查字元而非用 `str.isalnum()`，不夠 Pythonic |
| house-robber | **8** | DP (1D) | 基礎 1D DP 要 8 次才過，顯示 DP 直覺尚未自動化 |

### Tier 2：中等掙扎（6-7 次提交）

| 題目 | 次數 | 主題 | 備註 |
|------|------|------|------|
| two-integer-sum-ii | 7 | Two Pointers | 最終 OK |
| top-k-elements-in-list | 7 | Heap | 最終用 min-heap O(n log k)，正確 |
| minimum-stack | 7 | Stack/Design | 有 typo `preflixMin` |
| anagram-groups | 7 | Hashing | 用 sorted-key O(n·k log k)，可改 Counter tuple O(n·k) |
| string-encode-and-decode | 6 | Hashing | 多次換 delimiter 策略，早期版本有殘留 `print()` |
| products-of-array-discluding-self | 6 | Array | 最終 prefix/suffix 單陣列，最佳解 |
| merge-two-sorted-linked-lists | 6 | Linked List | 最終 OK |
| longest-consecutive-sequence | 6 | Hashing | 最終 set-based O(n)，正確 |
| kth-largest-element-in-an-array | 6 | Heap | 最終 heappushpop，正確 |
| is-anagram | 6 | Hashing | **用 sorted O(n log n)，應改用 Counter O(n)** |
| depth-of-binary-tree | 6 | Trees | 基本遞迴，最終 3 行，但花了 6 次 |
| buy-and-sell-crypto | 6 | Array | 最終 OK，但有 `preflixMin` typo |

### Tier 3：有掙扎（5 次提交）

| 題目 | 主題 | 關鍵問題 |
|------|------|----------|
| lowest-common-ancestor-in-BST | Trees/BST | **沒有利用 BST 性質，用了通用 BT 的 O(n) 解法而非 O(h)** |
| partition-equal-subset-sum | DP/Knapsack | 從 naive DFS 進化到 set-based DP |
| maximum-product-subarray | DP | 最終 currmin/currmax 同時追蹤，正確 |
| subtree-of-a-binary-tree | Trees | 缺少顯式 `return False`，依賴 None 的 falsy 行為 |
| largest-rectangle-in-histogram | Stack | 最終 monotonic stack O(n)，正確 |
| clone-graph | Graph/BFS | 最終 BFS + hashmap，正確 |
| valid-sudoku | Hashing | 最終用 bitmask，反而是進階解法 |

---

## 二、反覆出現的 Code Quality 問題

| 問題 | 出現在 | 面試影響 |
|------|--------|----------|
| **不利用資料結構特性** | LCA in BST 用通用 BT 解法 | 高 — 面試官會追問「能不能更快？」 |
| **用次優解** | is-anagram 用 sorted 而非 Counter | 中 — 不影響正確性但顯示不熟慣用法 |
| **一致性 typo** | `preflixMin` 出現在 2 個不同題目 | 低 — 但面試中會顯得粗心 |
| **隱式 return** | subtree-of-a-binary-tree 沒有顯式 return False | 中 — 面試官可能會問 |
| **Debug 殘留** | string-encode-and-decode 殘留 print() | 中 — 面試中要注意清理 |

---

## 三、各主題掌握度評估

### 主題熟練度總表（量化判定）

> **規則主導**：等級由下方「判定規則」自動計算，不靠主觀描述
> **由誰維護**：`/practice` 完成題目後增量更新（題數 +1、最近 2 題左移）；`/study` 開始時校正全表
> **被誰使用**：`/study` 選題時依 `等級` 欄直接挑 weak/gap 主題，不再從敘述文字推斷

| 主題 | 已解題數 | 最近 2 題 | SR 最高階段 | 等級 | 備註 |
|------|---------|----------|-----------|-----|------|
| Array / Hashing | 30+ | ✅✅ | — | proficient | 基本功扎實；歷史 anagram/sudoku 有掙扎但已鞏固 |
| Two Pointers | 8 | ✅✅ | — | proficient | 歷史 three-sum / palindrome 早期掙扎，最終 optimal |
| Stack / Monotonic Stack | 9+ | ⚠️✅ | 7d | **borderline** | 394 SR ✅ 大進步（iterative 三大卡點全解 + 自推 recursive index passing）；嵌套 parsing mental model 已建立 |
| Binary Search | 9+ | ⚠️✅ | 2d | **weak** | 162 ⚠️ 揭露 BS template（A: `l<r` vs B: `l<=r`）區分不熟；non-monotonic invariant 需引導 |
| Trees (general) | 19+ | ⚠️⚠️ | 2d | **weak** | 236 LCA ⚠️（第一版漏遞迴右子樹）；94 ⚠️ |
| BST | 3 | ⚠️✅ | 2d | **weak** | 230 Kth ⚠️；歷史 LCA 沒用 BST 性質 O(h) |
| Backtracking | 12+ | ✅✅ | — | proficient | subsets/permutations/combinations 全覆蓋 |
| Graph BFS/DFS | 15+ | ⚠️✅ | 2d | **weak** | 127 首次 Hard BFS ⚠️（BFS/wildcard 提示 + 複雜度漏算 slice cost）；14+ 題基礎仍在 |
| Union Find | 3 | ⚠️⚠️ | 2d | **weak** | 547 SR ⚠️（template 3 bug）+ 721 ⚠️（斷鏈 bug + 跨行 union 機制講不出）；UF template 肌肉記憶 + 「搬祖宗」union 寫法仍未穩固 |
| DP (1D) | 6 | ⚠️— | 2d | **weak** | house-robber 8 次；1235 weighted interval scheduling ⚠️（DP+BS hybrid，dp 偏移 1 沒貫徹） |
| DP (2D) | 2 | ⚠️⚠️ | 2d | **weak** | 64 ⚠️ 實作對但講不出「為什麼 1D work」；97 ⚠️ 邊界需引導 |
| DP (Knapsack) | 2 | ⚠️— | — | **weak** | 題數<3；partition-equal-subset-sum 5 次 |
| Heap | 3+ | ✅⚠️ | 2d | **weak** | top-k / kth-largest 早期 5-6 次；295 最近 ✅ |
| Monotonic Queue | 1 | ⚠️— | 2d | **weak** | 題數<3；239 首次接觸有 2 個實作 bug |
| Segment Tree / BIT | 0 | — | — | **gap** | 零覆蓋 |
| 進階 Design | 0 | — | — | **gap** | LFU / Iterator / Rate Limiter 未練 |
| Math | 0 | — | — | **gap** | 幾乎零覆蓋 |

### 等級判定規則

依序檢查，第一個符合的生效：

1. **gap**：已解題數 = 0
2. **weak**：以下任一成立
   - 已解題數 < 3（尚未鞏固）
   - 最近 2 題結果中有 ⚠️ 或 ❌
3. **proficient**：以下全部成立
   - 已解題數 ≥ 5
   - 最近 2 題結果皆為 ✅
4. **developing**：上述皆非（已脫離 weak，尚未達 proficient）

> 「最近 2 題」指該主題最新完成的兩題（依完成時間序），不是全域最近兩題。`—` 表示該主題題數不足 2。

### 質性分析（補充說明，不影響等級判定）

#### 歷史弱點脈絡
| 主題 | 歷史訊號 | 方向 |
|------|---------|------|
| DP | house-robber 8 次、partition-equal-subset-sum 5 次 | 2D DP、Knapsack 變體、State Machine DP |
| Union Find | count-connected-components 11 次，最大掙扎點 | UF template 肌肉記憶化 |
| BST 特性 | 舊 LCA 用通用 BT O(n) 而非 O(h) | 刻意練習利用 BST ordering |
| Heap | 基本 heap 題早期 5-6 次 | 已改善，鞏固中 |

#### Gap 對應的 Google 出題頻率
| 主題 | Google 頻率 |
|------|------------|
| Monotonic Queue | 高 |
| 進階 DP（distinct-subsequences、burst-balloons、regex-matching） | 中高 |
| 進階 Design | 中 |
| Segment Tree / BIT | 低但偶有 |
| Math | 低 |

#### 🔴 特別標記：Nested Parsing Stack Pattern（2026-04-18 新增）

- **卡點**：394 Decode String 重度卡關。根本問題是**無法 visualize 嵌套處理**（試圖同時想所有層）
- **心智模型**：stack = 手動管 call stack；每次只想「當前一層」的進入/處理/離開
- **相關題**：394、726、227、224、636、1096（全都是同一個 pattern）
- **筆記**：`notes/nested_parsing_stack.md`
- **下次 /study 優先納入**：227 Basic Calculator II（同 pattern 再練一題，鞏固模型）

#### 🔴 特別標記：Binary Search Template 區分不熟（2026-04-25 新增）

- **卡點**：162 Find Peak Element。Template A（`while l < r`, return l）vs Template B（`while l <= r`, return -1 / mid）的差別**不清楚**，導致 code 寫起來「靠感覺」而非依規則挑模板
- **判斷規則**（這次練習建立）：
  - **找位置 + 答案保證存在（invariant 維持）→ Template A**（如 162、278 First Bad Version、找最小滿足 X 的 index）
  - **找特定值 + 可能不存在 → Template B**（如經典 sorted array 找 target）
- **附帶弱點**：non-monotonic 陣列上 BS 的 invariant 需要引導推 case A/B 才能說服自己「為什麼丟一半安全」
- **equality 殺手**：當比較結果無法決定丟哪半（== 出現），BS 直接退化 O(n)。不是「換 if/else」可以救
- **相關題**：162、278、153 Find Min in Rotated、33/81 Search in Rotated、35 Search Insert、875 Koko、1011 Capacity to Ship、4 Median of Two Sorted Arrays
- **筆記**：`notes/binary_search_templates.md`（兩種 template 完全指南 + 練習路徑）
- **下次 /study 優先納入**：278 First Bad Version（純 Template A 鞏固）+ 33 Search in Rotated Sorted Array（Template B + invariant 進階）

---

## 四、語言轉換觀察

- **JS → Python 遷移**：44 題同時有 JS 和 Python 版本，JS 都是早期提交
- **2 題仍為 JS only**：`climbing-stairs`、`min-cost-climbing-stairs`（建議用 Python 重寫）
- **Python 版本明顯更簡潔**：JS 版本較冗長（手動 charCode 檢查等）

---

## 五、Google SWE L4 準備建議（優先排序）

### P0 — 立即處理
1. 重解 `lowest-common-ancestor-in-BST`，用 BST 性質 O(h)
2. 重解 `is-anagram`，用 Counter O(n)
3. 把 `climbing-stairs` 和 `min-cost-climbing-stairs` 用 Python 重寫

### P1 — 本週完成
4. Union Find template 肌肉記憶化：再練 `accounts-merge`、`graph-valid-tree` 變體、`number-of-provinces`
5. 做 `sliding-window-maximum`（Monotonic Queue）
6. 中等 DP 練習：`interleaving-strings`、`distinct-subsequences`
7. **DFS-based 有向圖環偵測（3-color / 3-state）**：207 SR 重做時改用 DFS，或練 802 Find Eventual Safe States、210 Course Schedule II（DFS 版）。Plan #4 #3 用 Kahn's BFS 寫對但 DFS 解法完全沒接觸過 — 面試 follow-up「用 recursion 寫」會卡

### P2 — 持續練習
7. 進階 DP：`burst-balloons`、`regular-expression-matching`
8. Design 題：`LFU Cache`、`Iterator` 類
9. 開始限時模擬面試（用 `/mock`），建立時間壓力下的表現

### P3 — 補充
10. Segment Tree / BIT 基礎了解（Google 偶爾出）
11. System Design 準備（coding 之外的另一半）

---

## 六、讀書計畫紀錄

> 每完成一份 5 題讀書計畫後，紀錄在此。用 `/study` 生成新計畫。

### Plan #3 — 2026-04-21 ~ 2026-05-01
主題重點：Stack nested parsing 鞏固、Union Find 肌肉記憶、DP + Binary Search 進階

| # | 題目 | 結果 | 花費時間 | 筆記 |
|---|------|------|----------|------|
| 1 | 162. Find Peak Element | ⚠️ | — | BS on non-monotonic array：invariant（升→右、降→左）需引導；Template A vs B 一開始混淆；equality follow-up 需多次 trace 才理解 BS 在 == 時崩潰 |
| 2 | 547. Number of Provinces (SR) | ⚠️ | — | 從首次 ✅ 退步。3 個 UF template bug：find 用 `==` 漏 path compression、union by rank 比 leaf 而非 root、掛 leaf 而非 root。需 review 才抓出 → 維持 SR 2d。Template 肌肉記憶仍未穩固 |
| 3 | 227. Basic Calculator II | ⚠️ | — | 首次 prev_op pattern。第一版「看到 +/- 就 drain」太繞、邊界錯（`1-1+1` 崩）。引導核心 insight：+/- 延後、*// 立即。雷：truncate toward zero 必須 `int(a/b)` 不是 `a//b`。Follow-up O(1) space 完成但 closure 變數誤用 |
| 4 | 721. Accounts Merge | ⚠️ | — | UF 進階。選 node 沒問題但**跨行 union 機制講不出**，需追問三次才答出 emailToIdx 橋樑。**核心 bug：`roots[i] = find(j)` 斷鏈**（鑽石 case 才爆）。思路第一版事實錯誤、複雜度也錯。新增 notes「斷鏈陷阱」+「hash map 當橋樑」 |
| 5 | 1235. Maximum Profit in Job Scheduling | ⚠️ | — | 首次 weighted interval scheduling Hard。**DP 定義初版錯**（i 是時間、forward push）需糾正為 backward「選/不選」。**漏不選分支**。**Index 偏移 bug**：dp 偏移 1 設計沒貫徹。修法後比建議更乾淨：`bisect_right` 直接當 dp index 自動處理 base case。BS Template 暖身回答錯但用 bisect_right 繞過。Stream follow-up 答對 |

**整體觀察：**
- **5 題全部 ⚠️**（與 Plan #2 同樣全 ⚠️），挑戰度拉對了但每題都需引導
- **共通 root cause：思路講解不精準**
  - #4 思路第一版「相同的 index」（事實錯誤）
  - #5 「i 是時間」（無法 work，10^9 開不下陣列）
  - #1 暖身回「找區間」（框架錯）
  - 寫 code 之前的口述常常有 hand-wave / 概念糊
- **共通 root cause：模板/設計意圖不貫徹**
  - #2 UF template 肌肉記憶 3 bug
  - #4 union 寫法搬「自己」而非搬「祖宗」（斷鏈）
  - #5 dp 偏移 1 的設計只在宣告時有，查表時又用 job index 查
- **新建心智模型**：UF「斷鏈陷阱」、「hash map 當橋樑」進階模式（已寫進 `notes/union_find_template.md`）
- **平均花費時間沒紀錄** — 5 題完成跨度 10 天但無單題計時，建議 Plan #4 開始計時

**下次建議加強：**
- **思路口述訓練**：寫 code 前必須能用 1-2 句講清楚 dp[i] 定義 / UF node 選擇 / BS invariant，不准 hand-wave
- **設計意圖一致性**：偏移 1、特判 -1 等設計選了就全程貫徹，不要寫一半變回 0-indexed
- 開始計時（Plan #4 起）+ 嘗試 `/mock` 模式建立時間壓力下表現
- DP + BS 同 pattern 變體（Russian Doll Envelopes #354、Longest Increasing Subsequence #300 with patience sort）

---

### Plan #2 — 2026-04-18 ~ 2026-04-21
主題重點：Tree/BST 對比學習、Stack 字串處理、2D DP 鞏固、Graph BFS 進階

| # | 題目 | 結果 | 花費時間 | 筆記 |
|---|------|------|----------|------|
| 1 | 64. Minimum Path Sum | ⚠️ | — | 1D 滾動實作對但講不出「為什麼 work」；dp 定義/邊界/轉移需多次引導；follow-up path reconstruction 方向 ok |
| 2 | 236. LCA of Binary Tree | ⚠️ | — | 核心 insight「左右都找到→root；只一邊→回傳那邊」對，但第一版漏遞迴右子樹；post-order 與 inorder 措辭混淆；follow-up parent pointer 誤答為 cycle detector |
| 3 | 394. Decode String | ⚠️⚠️ | — | **重度卡關**。無法 visualize 嵌套處理；iterative 版 `[` push 丟失外層 char、`]` pop 錯推 char。新增 `notes/nested_parsing_stack.md`。下次 /study 納入 227 Basic Calculator II |
| 4 | 235. LCA of BST (SR) | ⚠️ | ~10 min | iterative O(1) 概念需引導（先前只熟 recursive O(h)）；small/big normalize 寫法聰明；複雜度措辭 O(n) 應為 O(h)；殘留註解舊版未清 |
| 5 | 127. Word Ladder | ⚠️ | — | 首次 Hard BFS。需 BFS/wildcard 兩個提示起步，主架構一次過。複雜度寫 O(M·N) 應為 O(M·N²)。Visited 次優（pop 時 check 而非 enqueue 時 mark）。Bidirectional BFS follow-up 部分正確但誤答記憶體方向 + 漏 "expand smaller frontier" |

**整體觀察：**
- 5 題全部 ⚠️，其中 394 ⚠️⚠️（雙警示）。這份計畫**每題都有需引導點**，顯示挑戰度拉對了
- **共通 root cause**：**複雜度分析不精準**（64 講不出 dp[j] 對應關係、235 寫 O(n) 而非 O(h)、127 漏算 slice cost）。需要**在寫 code 前就口述精準複雜度**的習慣
- **Stack 主題從 proficient 掉回 weak**（394 重度卡關），nested parsing mental model 不穩
- **New 心智模型建立**：`notes/nested_parsing_stack.md`（抽屜+桌面類比），下次相似題測驗是否內化
- Follow-up 表現偏弱（236 parent pointer、127 bidirectional BFS）— 建議加強變體思考訓練

**下次建議加強：**
- 227 Basic Calculator II（同 394 pattern 鞏固）
- 721 Accounts Merge（UF 多題鞏固）
- 複雜度寫之前「先列出所有成本來源」的習慣（含 slice、key 儲存等容易忽略的）
- 開始限時 mock（Plan #2 無時間紀錄，說明平時練習沒測時間壓力）

---

### Plan #1 — 2026-04-11
主題重點：Union Find 肌肉記憶、2D DP 入門、Monotonic Queue 補缺口

| # | 題目 | 結果 | 花費時間 | 筆記 |
|---|------|------|----------|------|
| 1 | 230. Kth Smallest in BST | ⚠️ | — | recursive 能寫但不熟 iterative inorder，學了 stack 模板後重寫成功 |
| 2 | 547. Number of Provinces | ✅ | — | UF with path compression + union by rank，搞清楚 rank 語意 |
| 3 | 97. Interleaving String | ⚠️ | — | 第一次做 2D DP，需引導才能起頭，但 space 優化 O(n) 自己完成 |
| 4 | 295. Find Median from Data Stream | ✅ | ~15 min | two-heap pattern，幾乎不需要提示 |
| 5 | 239. Sliding Window Maximum | ⚠️ | ~20 min | 第一次接觸 monotonic queue，思路正確但有兩個實作 bug |

**整體觀察：** 熟悉的主題（BST、Heap）表現好且快。新概念（iterative inorder、2D DP、monotonic queue）需要引導才能起步，但理解後能自己寫出來。複雜度分析容易出錯（寫錯 O(log n) 和 O(n)），需要養成寫 code 前先講複雜度的習慣。
**下次建議加強：** 2D DP 再練 1-2 題鞏固（Edit Distance、LCS）、Monotonic Queue/Stack 再練一題、開始做限時 mock 測試面試壓力下的表現
