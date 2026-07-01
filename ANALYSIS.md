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
| Intervals | 2 | ⚠️⚠️ | 2d | **weak** | #56 Merge Intervals ⚠️（Plan #8，固定-end misconception → running-max）；#986 Interval List Intersections ⚠️（**mock #01**，雙指針 max/min 一次寫對且乾淨最優，但初版把 #56 merge 邏輯帶進來一 nudge 自修 + test 主動性仍缺）。題數<3 |
| Stack / Monotonic Stack | 9+ | ❌✅ | 7d | **weak** | **227 Basic Calculator II SR ❌ Fail 重置 2d（Plan #10, 6/16）**：需完整三變數骨架才動手（同 #235 chronic「講得出翻不成 code」）、卡點史減法 bug 再犯 `res-=lastNum`（`10-2-3`→-11）、**假 pass**（測資對稱抵銷）；394 SR ✅ 大進步（iterative 三大卡點全解）。近題含 ❌ → 退回 weak |
| Binary Search | 10+ | ⚠️⚠️ | 7d | **weak** | 162 Find Peak SR ⚠️ **Pass 升 7d**（6/13：4/25 兩痛點收掉——invariant「保證」兩結局窮舉 + Template by rule「找位置+保證存在→A」；equality 殺手 FU 獨立答對；⚠️ 因 clarifying precision + test 多解 hardcode）；875 Koko ⚠️（BS-on-answer）；33 ⚠️⚠️（雙重邊界 bug，trace 紀律弱項）；153 ✅（#33 紀律重做修復）|
| Trees (general) | 19+ | ⚠️⚠️ | 7d | **weak** | 236 LCA SR ⚠️ **Pass 升 7d**（6/13：4/18 漏右遞迴 bug 未復發、複雜度主動精準、post-order why + FU 方向對；⚠️ 因 clarifying 問低價值 + 思路漏 base case + O(1) sign-marking 忘 val 範圍）；94 ⚠️ |
| BST | 4 | ✅⚠️ | 2d | **weak** | 235 LCA SR ⚠️（6/11：開場又用通用 BT O(n)、iterative O(1) 仍需引導——4/20 同模式重演；自選 root==p 殺手測資質高）；230 Kth ⚠️ |
| Backtracking | 12+ | ✅✅ | — | proficient | subsets/permutations/combinations 全覆蓋 |
| Graph BFS/DFS | 17+ | ⚠️⚠️ | 7d | **weak** | **994 Rotting Oranges ⚠️（mock #02, 2026-07-01, 40min）**：multi-source BFS + counter 終止**自己想到**、方向 trick 乾淨、complexity 一 nudge 修對，但 **真 bug 未被自己測出**（`if not tmp:return 0` 對 fresh-but-no-rotten 回 0 應 -1，且此 case **學生 clarifying 親口問過卻沒寫成 test＝clarify→test 斷層**）＋ 4 given test 假 pass ＋ 首次修引入 off-by-one（minutes++ 移 wave 尾多算末層 → Case 1 得 5）；需面試官指行才修。127 Word Ladder SR ⚠️ **Pass 升 7d**（6/14：零提示自到 Graph+BFS、Time 主動 O(M·N²)；⚠️ 因 Space 又犯 O(M) 盲點 + bidirectional BFS follow-up 跳過）；210 Course Schedule II ⚠️（DFS 3-color cycle 首次，in-degree 機關致不相連環漏判 + test 紀律）；863 ✅ Tree→Graph BFS |
| Union Find | 4 | ✅⚠️ | 7d | **weak** | **547 SR ✅ 升 7d（Plan #10, 6/15）**：template 一次寫對、零 4/27 卡點史 bug（find path-halving / union 先 find 兩 root / 只掃上三角）；684 ⚠️（首次 find+union canonical、零 547/721 bug，但概念 nudge：exactly-one→early return / O(n·α) / invariant 循環）；721 ⚠️（斷鏈）。近 2 題 ✅⚠️ 仍 weak（含 ⚠️），但 template 肌肉記憶已達標，弱點上移到思路/優化精準度 |
| DP (1D) | 6 | ⚠️— | 2d | **weak** | house-robber 8 次；1235 weighted interval scheduling ⚠️（DP+BS hybrid，dp 偏移 1 沒貫徹） |
| DP (2D) | 3 | ⚠️⚠️ | 7d | **weak** | 64 SR **Pass 升 7d**（6/11：invariant/dp 定義/in-place 安全/1D dp[j] 對應口述全達標——4/18「寫得出講不出」收掉；label ⚠️ 僅因事前 gate 講不出失誤面）；97 ⚠️ 邊界需引導 |
| DP (Knapsack) | 4 | ✅✅ | 2d | **developing** | **518 Coin Change II ✅（Plan #10, 6/17, 新題）**：#322 彩蛋成功遷移——loop order 外 coins/內 amount=組合，自選對且**講得出 WHY** + 正確反例，recurrence/base/複雜度全自主一次過；322 Coin Change ✅ 首次 unbounded knapsack；partition-equal-subset-sum 5 次。近 2 題 ✅✅ 脫離 weak，題數 4<5 未達 proficient |
| Sliding Window | 2 | ✅✅ | 2d | **weak** | 3 Longest Substring ✅（Plan #7 #1，last-seen-index variant）+ 76 Min Window ✅（Hard）；題數<3 仍需鞏固（209/424 待做） |
| Hash + Prefix Sum | 2 | ⚠️⚠️ | 2d | **weak** | 525 Contiguous Array ⚠️（Plan #7 #2，±1 transform；hashmap value=index 語意卡）+ 560 Subarray Sum K ⚠️（value=count）；題數<3 |
| Heap | 5+ | ⚠️⚠️ | 2d | **weak** | **621 Task Scheduler ⚠️（Plan #10, 6/16, 新題）**：兩解都討論（heap + math），greedy 方向自抓但 math 公式漏 countOfMax/漏 max(,len) 需反例逼出、why-greedy 偏淺，最終 O(L)/O(1) 乾淨正確；295 SR ⚠️（漏 order rebalance 自 trace `[5,1,10]` 抓回、invariant「差2」當 state、複雜度兩處不精確）；23 Merge k Lists ⚠️（heap+LL Hard、Python comparison 坑）；973 ✅ 首解。**973 SR-burndown 重做 ⚠️（Plan #11 #1, 7/1）**：max-heap 核心零提示＋主動用 `heappushpop` 合併 sift＋主動加 origin edge case；但 sqrt 單調性需二度追問、follow-up O(n) 揭露 **partition 機制整個沒學過**（非僅不知 quickselect 名稱），一度把 quicksort/quickselect 行為講反後自己修正對 → 新增 `notes/quickselect_partition.md` + 下方新 gap 主題 |
| Monotonic Queue | 1 | ⚠️— | 2d | **weak** | 題數<3；239 首次接觸有 2 個實作 bug |
| Segment Tree / BIT | 0 | — | — | **gap** | 零覆蓋 |
| 進階 Design | 0 | — | — | **gap** | LFU / Iterator / Rate Limiter 未練 |
| Math | 0 | — | — | **gap** | 幾乎零覆蓋 |
| Sorting / Quickselect | 0 | — | — | **gap** | **973 follow-up 揭露（7/1）**：partition 機制完全沒學過（非僅不知 quickselect 名稱）。已建立 `notes/quickselect_partition.md`；下次 /study wildcard 槽位可排 215. Kth Largest Element 當入門題 |

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

> ⚠️ Plan #5、#6、#8 的摘要尚未回填到此 section（計畫檔在 `study/`，逐題結果在 `review/schedule.md`）。下次有空可補。

### Plan #10 — 2026-06-14 ~ 2026-06-21（正常結構：2 weak + 2 review + 1 Google）
主題重點：UF / Stack-parsing 最老 SR backlog（overdue 45–46 天）、Heap 弱項、DP-Knapsack 弱項（#322 loop-order 對照）、Google 🔥🔥🔥 String 校準（edge-case + clean-code 硬題）。全程避開 Plan #9 主題。

| # | 題目 | 結果 | 花費時間 | 筆記 |
|---|------|------|----------|------|
| 1 | 547. Number of Provinces (SR) | ✅ | ~暖身快速 | **Pass 升 7d**。UF template 一次寫對、零 4/27 卡點史 bug（find path-halving / union 先 find 兩 root / 只掃上三角）。parent 初始值口誤秒改。缺：test 失敗點口述偏淺 |
| 2 | 621. Task Scheduler | ⚠️ | 含討論較久 | 新題、Heap 弱項。兩解都討論（heap + math）。greedy 方向自抓，但 math 公式漏 countOfMax、漏 max(,len) 需反例逼出；why-greedy 偏淺。最終 O(L)/O(1) 乾淨正確。思路初版留 TODO。SR 2d |
| 3 | 227. Basic Calculator II (SR) | ❌ | 含 debug 較久 | **Fail 重置 2d**。需完整三變數骨架才動手（同 #235 chronic 性質）；卡點史減法 bug 再犯 `res-=lastNum`（`10-2-3`→-11）；**🔴 假 pass**（測資對稱抵銷、bug 助教抓非自抓）。修法符號綁項上 `lastNum=-num`、結算永遠 += |
| 4 | 518. Coin Change II | ✅ | 順暢 | 新題、Knapsack combinations。**#322 彩蛋成功遷移**：loop order 外 coins/內 amount=組合，自選對且講得出 WHY + 正確反例。recurrence/base/複雜度全自主、一次過 canonical。follow-up 排列版對調迴圈一句命中。缺：test gate 沒口述失敗點。SR 2d |
| 5 | 68. Text Justification | ⚠️ | 非限時（帶成品 debug+重構）| 新題、Google 🔥🔥🔥 Hard。帶會跑但 Case 1 fail 成品來。Bug=空格分配三元式優先序錯（needOneMore 歸零後 baseSpace 被丟）。**code quality 三輪重構**（抽 helper → 名字接反+self.ans+closure 依賴 → 殘留 closure 未收）。**亮點：複雜度 Space 主動分 aux vs output 兩者皆對——#127 盲點未犯**；單字行 corner case 自補。缺：思路 1 段、無 clarifying、無 test gate（帶成品性質）。Hard 新題 SR 納入 2d |

**整體觀察：**
- **結果 ✅⚠️❌✅⚠️**（2 ✅ + 2 ⚠️ + 1 ❌）。SR 複習 2 題：#547 升 7d、#227 Fail 重置；新題 3 題（#621 / #518 / #68）全納入 SR。
- **#227 是本份最大警訊**：減法符號 bug **第二次**重演（首解 + 本次），且**假 pass**（對稱測資抵銷）模式與 #33 / #210 同源——「測資沒打到失敗點 → All tests passed 是假象」。根因是「心智模型講得出、翻不成 code」（同 #235 chronic），需練到不靠骨架。
- **彩蛋/遷移成功**：#518 把 #322 記的「loop order 外 coins=組合、反之=排列」彩蛋完整遷移，講得出機制 + 反例，是跨題知識複用的正面案例。
- **複雜度 Space 盲點這次沒犯**（#68 主動分 aux vs output 兩者皆對）——對比 Plan #9 #127 的 O(M)→O(M·N) 失誤是明確進步；但僅在「被當 forcing function 主動問」時觸發，尚未證明會自動做。
- **code quality 深練一次**（#68）：從一坨 → 抽 helper → 修命名 / 解耦，三輪才到 production-ready。**命名接反**（helper 名字與行為相反）是新出現的反模式，比 `tmp` 模糊更糟（主動誤導）。L4 bar「production-ready、every corner case」這題練到重點，但「一次就乾淨」尚未做到。
- **test 紀律退回半套**：#547 / #518 都「沒主動口述事前 test gate 打哪個失敗點」，#68 因帶成品來連 gate 都沒走。對比 mock #01 / Plan #9 的進步本份退步——可能因 3/5 題是「複習 / 帶成品」而非從零，gate 自然鬆。

**下次建議加強：**
- **🔴 #227 減法 bug + 假 pass 是必修**：下次 SR（已 due 6/18）開口直接「符號綁項上 `lastNum=-num`、結算永遠 +=」+ 事前 gate 必含非對稱 case `10-2-3` / `10-6-3`。再犯視同 chronic。
- **「心智模型→code」翻譯練習**（#227 / #235 共同 chronic）：能講不能寫，下次這兩題不給骨架、逼從零起手。
- **複雜度 Space 主動化**：#68 證明「被問就會對」，目標是不問也主動分 aux vs output（延續 Plan #9 建議）。
- **事前 test gate 回正軌**：#547 / #518 / #68 都沒主動口述失敗點，下次從零題開口就要「哪個 case 打爆我」。
- **#68 字串用 ''.join**（#394 同課）+ helper 一次命名對齊行為，下次 String / refactor 題注意。
- **🔴 mock cadence 觸發**：mock #01（6/09）後已完成 Plan #9 + #10 = **2 份計畫** → 下次 `/study` 預設先跑一場 45 min `/mock` 再開新計畫（題目從已練主題抽，量壓力下體檢），學生明確說「跳過」才略過。

### Plan #9 — 2026-06-09 ~ 2026-06-14（SR-burndown）
主題重點：清最久未複習的 backlog（overdue 43–54 天），橫跨 BST / 2D DP / Tree / Binary Search / Graph-BFS。mock #01 後第一次 practice，驗證 test 紀律在無人 push 下是否成立。

| # | 題目 | 結果 | 花費時間 | 筆記 |
|---|------|------|----------|------|
| 1 | 235. LCA of BST (SR) | ⚠️ | ~52 min wall | **唯一沒升階（維持 2d）**。開場又用通用 BT O(n)、BST ordering + iterative O(1) 均需引導——**4/20 同模式第三次重演**。自選殺手測資 root==p 質高。done 紀律弱（思路-code 不對齊、死 code 兩度未刪）|
| 2 | 64. Minimum Path Sum (SR) | ⚠️ | ~22 min wall | **Pass 升 7d**。4/18「寫得出講不出」全收——invariant 狀態版 / dp 定義 / 邊界 / in-place 安全 / 1D dp[j] 對應全口述達標。label ⚠️ 僅因事前 gate 兩次講不出失誤面 |
| 3 | 236. LCA of Binary Tree (SR) | ⚠️ | ~12 min | **Pass 升 7d**。4/18 漏右遞迴 bug 未復發、自加 case 4 精準守舊傷口、複雜度主動精準、post-order why + FU 方向對。⚠️：clarifying 問低價值 / 思路漏 base case / O(1) sign-marking 忘 val 範圍 |
| 4 | 162. Find Peak Element (SR) | ⚠️ | ~10 min | **Pass 升 7d**。4/25 兩痛點收掉——invariant「保證」兩結局窮舉 + Template by rule（找位置+保證存在→A）；equality 殺手 FU 獨立答對。⚠️：clarifying precision（全 unique→相鄰不等）/ test 多解 hardcode |
| 5 | 127. Word Ladder (SR) | ⚠️ | ~18 min | **Pass 升 7d**。4/21 兩痛點收掉——零提示自到 Graph+BFS、Time 主動 O(M·N²) 含建字串項。⚠️：Space 又犯同盲點 O(M)→O(M·N) / 思路初版空白 / count+1 理由初版湊 / bidirectional BFS follow-up 初版想跳過、提示後**補做答對核心**（擴展較小邊界=4/21 漏點，記憶體更少修正 4/21），但 why（量化 + 挑小邊理由）仍需 push |

**整體觀察：**
- **5 題全 ⚠️ label，但 4/5 升階（2d → 7d）**——這正是 SR「升階看 outcome 不看 label」設計的體現：核心解時間內寫對就升，⚠️ 只記重做要點。這份 burndown 真的把長期卡 2d 的老題往前推了，retention 比帳面分數好很多。
- **唯一沒升的 #235** 是真問題：BST ordering + iterative O(1) **連三次（4/20、6/11、本次）都需引導**，已是 chronic。下次再犯應視同 Fail 重置 + 當 burndown 必選。
- **複雜度主動性大進步**：#64 / #162 / #127 的 Time 都主動講對，不需追問（對比早期 plan 的「複雜度漏項」root cause）。**但 #127 暴露新盲點**：「存/建一個字串成本 O(N) 非 O(1)」——Time 記得算、Space 又忘（O(M) 應 O(M·N)）。
- **test 紀律延續 mock #01 的進步**：#236 case 4（守舊 bug）、#162 自抓 hardcode 脆弱、#127 case 6 正確，三題都主動加 test 且品質可。**但「加 test 時口述打哪個失敗點」仍需 push**——事前 gate 只做到一半。
- **共通 root cause（壓力下鬆動）**：思路-code 對齊（#235 / #236 漏 base case / #127 思路空白）、口述精準度（#127 count+1 初版湊理由、#162 template 背對應表）、clarifying 精準度（#236 / #162 問的不是改變解法的那個保證）。這些都是「會寫、講不夠精準」，不是不會。
- **follow-up 軌跡分歧**：#162 equality 殺手獨立答對（4/25 是要 trace 才懂）；#127 bidirectional BFS 初版想跳過、提示後**補做且答對核心**（「擴展較小的當前層邊界」=4/21 真正漏點、記憶體更少修正 4/21「更多」），但 why（快的量化 / 挑小邊理由）仍停在直覺版需 push。

**下次建議加強：**
- **#127 bidirectional BFS 已補做（核心對）**：下次 SR 把 why 從直覺版升級到量化版——快（單向 `b^d` → 雙向 `2·b^(d/2)`，指數砍半≈開根號）、**每步展開較小的當前層邊界**（避免單邊指數爆炸）、記憶體更少。開口直接給，不要停在「可能性變少」。
- **🔴 #235 視同 chronic**：下次 burndown 必選，開口第一句就要是「BST ordering 下沉 + iterative O(1)」，再需引導即 Fail 重置。
- **複雜度 Space 也要套「字串/物件佔多少」**：不只 Time。#127 的 O(M·N) 盲點。
- **事前 test gate 補完整**：加 test 的同時**口述它打哪個失敗點**（目前只做到「有加」）。
- **下一份回正常結構**（不可連續 2 份 burndown）：2 weak + review 槽（依 backlog 自適應）+ Google 校準 + wildcard。但 backlog 仍大（session 起始 33 due），review 槽會吃較多。
- mock cadence：mock #01（6/09）後已完成 1 份計畫；距下次「≥ 2 份計畫」門檻還差 1 份，下下次 /study 需留意。

### Plan #7 — 2026-05-24 ~ 2026-05-30
主題重點：Sliding Window 鞏固、Hash+Prefix Sum 鞏固、DP 2D SR（39 天 overdue）、DFS Cycle Detection gap、Heap+LL Hard

| # | 題目 | 結果 | 花費時間 | 筆記 |
|---|------|------|----------|------|
| 1 | 3. Longest Substring Without Repeating Characters | ✅ | ~15 min | Sliding window last-seen-index variant 首次。4-段 forcing function **起作用**（被 push 後補完兩條 clean invariant）。「abba」stale-index trap 一發點破。Code 風格選 clever-over-defensive（Plan #8 起預設選 defensive）|
| 2 | 525. Contiguous Array | ⚠️ | ~30 min | Hash+Prefix 第 2 題。±1 transform 即答，但中段卡 hashmap value 語意（index vs count），4 步 Socratic 才補。4-段被 push。**Catch 助教 Space 錯誤 ✓** |
| 3 | 97. Interleaving String (SR) | ⚠️ | ~25 min | 39 天 overdue SR 重做。**vs Plan #1「邊界需引導」明顯進步**（自己起頭 + swap-to-shorter + 1D 滾動）。Q4 O(min) 優化卡、Q5 overlapping subproblems 講不出病因（已存記憶 quiz）。4-段半破（只貼 Section 1）|
| 4 | 210. Course Schedule II | ⚠️ | ~40 min | DFS 3-color cycle detection gap 首次（補 P1 #7）。思路 4 段**大進步**。但 code 加 in-degree 機關致不相連環漏判 bug + 假 pass。**test 紀律連 4 次未加 regression**。post-order vs pre-order 用反例講通 → notes 新增 |
| 5 | 23. Merge k Sorted Lists | ⚠️ | ~30 min | Heap+LL Hard 首次。**Code 全場最乾淨**（node-in-tuple + idx tie-break + dummy head one-pass）。Python comparison 坑需助教提。**思路與 code 不符（兩個 vs 三個元素，Plan #4 124 重演）+ test 紀律連 5 次**。沒提 divide & conquer |

**整體觀察：**
- **結果 ✅⚠️⚠️⚠️⚠️**（1 ✅ + 4 ⚠️）。每題都有需引導點，挑戰度拉對。
- **4-段思路 forcing function（本 plan 新規則）效果分層**：#1 起作用、#2 #3 被 push、#4 大進步（一開口 edge 方向 + 三色 invariant）、#5 思路與 code 不符。整體**比 Plan #4/#6 的「思路偏薄」進步**——forcing function 把問題從「事後提醒」變「事前 gate」，但仍需助教 push 才完整，未內化成自動行為。
- **🔴 新浮現的最大弱項：test 紀律**。#210 與 #23 共 ~5 次「明確要求自己加 test 卻不加 / 加錯」。延續 ANALYSIS 既有的 **trace 紀律**弱項（#33/#322/#560），現在擴大為「**寫前不主動想『哪個 input 打爆我』**」。#210 的 in-degree bug 正是因為沒有 disconnected-cycle 測試而被「All tests passed!」假 pass 掩蓋。
- **思路與 code 不符**（#23）是 Plan #4 (124) 就點過的老問題重演——口述/書寫精準度在壓力下仍會鬆。
- **新建心智模型**：±1 transform（#525）、**DFS 3-color cycle detection + post-order/reverse 拓撲序**（#210，`notes/dfs_topological_sort.md` 新增，含 pre-order 反例）、heap-of-k merge + Python tuple comparison 坑（#23）。
- **SR 里程碑**：#97 積壓 39 天終於重做，且明顯進步。但 SR backlog 仍在擴大（本 plan 又新增 #210 #23）。

**下次建議加強：**
- **🔴 把「自己寫 test」做成 forcing function（Plan #8 最高優先）**：比照 4-段思路，把「寫前先口述『哪個 edge case 會打爆我』+ 寫完前必須有 ≥1 個自己加的 assert」設成**事前 + 事後雙 gate**。光靠事後提醒已證明連 5 次無效。
- **思路一寫就跟 code 對齊**：tuple 幾個元素、return type、變數作用域——寫完回頭比對思路與 code（Plan #4 已建議、#23 仍犯）。
- **Code 風格預設 defensive**（Plan #8 起）：#1 的 clever max-placement 之後預設選標準寫法。
- **SR backlog 處理**：26+ → 更多。認真考慮 plan #7 筆記提的三個選項（SR-only 短 plan / 拉長槽位 / 30d-overdue 自動退階）。
- **轉 /mock 測壓力**：多題超時間目標（#2 #4），且 forcing function 在無人 push 時是否仍成立未知——mock 模式可驗證。

### Plan #4 — 2026-05-01 ~ 2026-05-05
主題重點：BST inorder 鞏固、Heap 經典、Graph topo sort 新 pattern、DP 經典、Tree Hard 挑戰

| # | 題目 | 結果 | 花費時間 | 筆記 |
|---|------|------|----------|------|
| 1 | 230. Kth Smallest in BST (SR) | ⚠️ | — | recursive inorder + early return 寫對且 tests pass，但 (1) 複雜度錯寫 Time O(n)/Space O(log n) 應為 O(H+k)/O(H) 沒考慮 skewed (2) `count=[k]` 用 list 包 int 沒講為何不用 nonlocal (3) truthiness trap：return node 物件剛好沒事，但若 return val 會被 val=0 騙到 — 未口頭點出 (4) follow-up（修改頻繁時優化）未答 |
| 2 | 973. K Closest Points | ✅ | — | max-heap of size k 一次寫對；`(-dis, i)` idx 當 tie-breaker 細節到位。Gap：(1) 沒主動講 max-heap vs min-heap 直覺 (2) 不知 quickselect 名稱 (3) sqrt 跳過數學依據（monotonic + 非負）講太籠統 |
| 3 | 207. Course Schedule | ✅ | — | 首次 Kahn's algorithm，自己推導 in-degree + BFS 核心。Code 第一版冗餘：visited set 多餘、BFS-by-level 結構也多餘（topo sort 不分 level）。複雜度 O(E) 漏算 V 應為 O(V+E)。**DFS-based 3-color cycle detection 完全沒接觸過** → ANALYSIS P1 #7 |
| 4 | 300. Longest Increasing Subsequence | ⚠️ | 10 min | DP + BS 兩版過 7 cases。**DP 卡點**：dp[i] 定義初版模糊未錨定 ending at i，需引導；答案是 max(dp) 非 dp[-1]。**BS 全新 pattern**：初次誤判為 mono stack，用 [0,1,0,3,2,3] 反例破解；tails 演算法 + invariant 從零教學。**思路 3 段需多次精確化**（tails 定義 / 為何嚴格遞增 / 為何覆寫安全），初版「紀錄最大長度 list」帶過明顯不夠 |
| 5 | 124. Binary Tree Maximum Path Sum | ⚠️ | 10 min | Hard 但極快（< 40 min 目標）。Code 一次過 7 cases。**核心 insight 對**：分開維護回傳值（一條腿）與全局 max（兩腿折返）+ 用 max(腿, 0) 處理負腿。Q-A/B 不對稱口述對、Q-D self vs tuple 理由具體。**問題**：(1) 思路書寫與 code 不符（寫「return [...]」但 code 用 self.）(2) Code 正確但繁瑣（4 候選列舉 vs 個別淨化腿的乾淨寫法）(3) 沒主動 clarifying，被列點問才答 |

**整體觀察：**
- **5 題 ⚠️✅✅⚠️⚠️**（3 ⚠️ + 2 ✅），比 Plan #3 進步（Plan #3 全 ⚠️）
- **首次單題計時**（Plan #4 起新規則）：300 與 124 都 10 min，遠超 Medium <25 min / Hard <40 min 目標。**速度建立但伴隨思路書寫鬆散**——快但口述不精準
- **新建心智模型**：
  - **Kahn's topological sort**（in-degree + BFS）→ 自推核心邏輯
  - **Patience sort / tails invariant**（LIS O(n log n)）→ 完整建立「tails[k] = 長度 k+1 的最小結尾」+ 砍結尾論證 + 覆寫安全雙段論證
  - **Tree split-at-node**（124 兩腿折返 vs 一腿延伸）→ 不對稱原因清楚
- **共通 root cause：思路文字書寫鬆散**
  - 207 思路寫得 OK 但複雜度漏 V
  - 300 「紀錄最大長度 list」初版幾乎無資訊量
  - 124 寫「return [...]」但 code 沒 return tuple——書寫與實作不同步
  - Plan #3 已點出此問題，Plan #4 仍重複出現
- **共通 root cause：Code 第一版常列舉 case 而非提煉 pattern**
  - 207：visited set + BFS-by-level（多餘的安全網）
  - 300 第一版：`max([0]+[...])` 用 list 拼接避免空 list
  - 124：`max(...resL+v+resR, v, v+resL, v+resR)` 列 4 case 而非用 `max(腿, 0)` 個別淨化
- **首次速度紀錄**：M 約 10 min（300 DP+BS 兩版）、H 約 10 min（124）。建議下次 mock 模式驗證有時間壓力時是否仍能維持

**下次建議加強：**
- **思路書寫精準性**：寫 code 後**回頭檢查思路與 code 是否同步**，特別是 return type、變數作用域
- **Code review 自我檢查**：寫完跑過後問自己「有沒有列舉的 case 可以用一個操作收掉？」（max(x, 0) 是經典 pattern）
- **主動 clarifying questions**：mock 模式下強制練習主動提問（不要等被問才答）
- 207 SR 重做時用 **DFS 3-color cycle detection** 補新解法
- 300 SR 重做時口述完整 tails invariant（3 段論證）
- 124 SR 重做時用「個別淨化腿」乾淨寫法
- 平均速度太快（Hard 10 min）建議轉入 mock 模式測試壓力下表現

---

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
