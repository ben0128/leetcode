# Spaced Repetition Schedule

> **目的**：把做過的題目轉成長期記憶，避免「做過就忘」
> **依據**：Red-Green-Code doubling-interval 間隔重複；interleaving 研究（Rohrer & Taylor 2007）
> **機制**：首次解題後排程 2d → 7d → 16d → 32d → mastered
> **更新**：每次 `/practice` 完成複習後，skill 自動維護此檔

---

## Active（待複習）

| # | 題目 | 難度 | 主題 | 首次日期 | 首次結果 | 當前階段 | 下次日期 | 備註 |
|---|------|------|------|----------|----------|----------|----------|------|
| 94 | Binary Tree Inorder Traversal | M | Tree / Stack | 2026-04-12 | ⚠️ | 2d | 2026-05-09 | iterative inorder 首次。2026-05-07 SR 複習 ⚠️：code 一次過 5 cases，但思路初版過薄（「左中右查找, 透過stack」未含 invariant）。Q1 invariant 答太弱（「每個 node 的 left 已推入」抓到表面但不夠強），Q2/Q3 答對結果但未解釋「為什麼不漏」。需 3 輪 Socratic + 具體 trace + 多選題（A/B/C 選項逼出 stack 頂端左子樹完整 visit 完）才升級到強化版。最終思路修為「pop 時已確認左子樹被走完, 所以可以安心訪問右側」抓到關鍵 invariant。SR 重做要點：(1) 開口就要直接講「pop 那一刻，左子樹保證已 visit 完」 (2) `while curr or stack` = 「還有路走 OR 還有債還」(3) `curr=node.right` 不漏的論證：左+自己都做完，剩右 → 維持 2d |
| 230 | Kth Smallest Element in BST | M | Tree / BST | 2026-04-12 | ⚠️ | 2d | 2026-05-04 | 2026-05-02 SR 複習 ⚠️：recursive inorder + early return 寫對且 tests pass，但 (1) 複雜度錯寫 Time O(n)/Space O(log n)，正解 O(H+k)/O(H)，沒考慮 skewed tree (2) `count=[k]` 用 list 包 int 沒講為何不用 nonlocal (3) truthiness trap：return node 物件剛好沒事，但若 return val 會被 val=0 騙到 — 未口頭點出 (4) follow-up（修改頻繁時優化）未答 → 維持 2d |
| 235 | Lowest Common Ancestor of BST | M | Tree / BST | 2026-04-11 | ✅ | 2d | 2026-04-22 | 2026-04-20 複習 ⚠️（需引導 iterative O(1) space；複雜度措辭 O(n) 應為 O(h)）→ 維持 2d |
| 547 | Number of Provinces | M | Union Find | 2026-04-12 | ✅ | 2d | 2026-04-29 | 2026-04-27 SR 複習 ⚠️：3 個 UF template bug（find 用 == 漏 path compression、union by rank 比 leaf 而非 root、掛 leaf 而非 root），測資簡單沒爆出來 → 維持 2d。Template 肌肉記憶仍未穩固 |
| 97 | Interleaving String | M | 2D DP | 2026-04-13 | ⚠️ | 2d | 2026-04-15 | 第一次 2D DP，邊界需引導 |
| 295 | Find Median from Data Stream | H | Heap | 2026-04-13 | ✅ | 2d | 2026-04-15 | two-heap pattern |
| 239 | Sliding Window Maximum | H | Monotonic Queue | 2026-04-13 | ⚠️ | 2d | 2026-04-15 | 首次 monotonic queue，有兩個實作 bug |
| 64 | Minimum Path Sum | M | 2D DP | 2026-04-18 | ⚠️ | 2d | 2026-04-20 | 1D 滾動實作對但講不出「為什麼 work」；dp 定義/邊界/轉移需引導精準 |
| 236 | LCA of Binary Tree | M | Tree / Recursion | 2026-04-18 | ⚠️ | 2d | 2026-04-20 | 第一版 code 漏遞迴右子樹；post-order 與 inorder 措辭混淆；follow-up LL intersection 方向錯 |
| 394 | Decode String | M | Stack / Nested Parsing | 2026-04-18 | ⚠️⚠️ | 7d | 2026-05-09 | 2026-05-02 SR ✅ 大進步：iterative 版三大上次卡點全解（多位數累積 / `[` push `[word, num]` / `]` formula `lastW + word*lastN`）一次寫對。Recursive 版自推 index passing pattern（`return (word, idx)`）。挑戰後改用 list + ''.join() 避 O(N²) string concat。剩餘小 nit：思路文字仍寫「for 迴圈」實際 while + return shape 一開始不一致（已修為統一 `[word, idx]`）。Mental model 已建立，進階 7d |
| 127 | Word Ladder | H | Graph / BFS | 2026-04-21 | ⚠️ | 2d | 2026-04-23 | 首次 Hard BFS。主架構一次過，但需 BFS/wildcard 兩個提示起步。複雜度錯寫 O(M·N) 應為 O(M·N²)（漏算 slice 與 key 長度）。Visited 次優（pop 時 check 而非 enqueue 時）。Follow-up bidirectional BFS 誤認為「記憶體更多」+ 漏掉 "expand smaller frontier" |
| 162 | Find Peak Element | M | Binary Search | 2026-04-25 | ⚠️ | 2d | 2026-04-27 | BS on non-monotonic array。Invariant（升→右、降→左）需引導推 case A/B；Template A vs B 差別一開始不清；equality follow-up 需多次 trace 才理解「== 時 BS 崩潰，degrade O(n)」非「換 else 就好」 |
| 227 | Basic Calculator II | M | Stack / Parsing | 2026-04-28 | ⚠️ | 2d | 2026-04-30 | 首次 prev_op pattern。第一版自創「看到 +/- 就 drain」太繞、邊界錯（`1-1+1` 崩）。需引導核心 insight：+/- 延後、*// 立即 → 變數設計：prev_op + 累積 num。雷：truncate toward zero 必須 `int(a/b)` 不是 `a//b`（負數會差 1）。Follow-up O(1) space（res + lastNum）已寫過：但寫的時候 `*///` 分支誤用 closure 的 `num` 而非參數 `value`，雖然測資沒爆但概念錯（call site 剛好讓 num==value）→ 已修。**SR 重做時要從 O(1) 版本起步**，不是 stack 版 |
| 721 | Accounts Merge | M | Union Find / Hash Map | 2026-05-01 | ⚠️ | 2d | 2026-05-03 | UF 進階應用。**選 node 沒問題（row index）但講不出跨行 union 機制** — 反覆說「行跟行 union」hand-waving，需追問三次才答出 emailToIdx[email]=row 是橋樑。**核心 bug：寫成 `roots[i] = find(j)` 而非 `roots[find(i)] = find(j)`** — 第二次 union 直接覆蓋自己 parent，把之前那條鏈砍掉。3 個原始測資都過（鑽石型 case 缺漏），加上 row 2 同時連 row 0/row 1 的 case4 才爆。思路第一版事實錯誤（「相同的 index」應為「相同的 email」）。複雜度首次寫 O(n²logn) 也錯。**SR 重做時重點：(1) 跨行 union 機制要直接講出 emailToIdx 橋樑 (2) 寫 union 時 `find` 兩邊** |
| 1235 | Maximum Profit in Job Scheduling | H | DP + Binary Search | 2026-05-01 | ⚠️ | 2d | 2026-05-03 | 首次 weighted interval scheduling（Hard）。**DP 定義初版錯**（「i 是時間」+ 想 forward push）需糾正為 backward「選/不選」。**漏「不選」分支**第一版強制每 job 都選。**Index 偏移 bug**：dp 偏移 1 沒貫徹，`dp[prevValidJobIdx]` 直接用 job index 查 dp 把前面 profit 整個丟掉。修法後**比建議更乾淨**：`bisect_right(endTimes, s)` 直接當 dp index，bisect=0 時 dp[0]=0 自動 base case，不用特判 -1。BS Template 暖身回答錯（「找區間」框架不對）但用 bisect_right 繞過手寫。Stream follow-up 答對。**SR 重做要點：(1) DP state 講清楚（"前 i+1 jobs max profit"）(2) 「選/不選」雙分支 (3) 偏移 1 設計就要全程貫徹** |
| 973 | K Closest Points to Origin | M | Heap | 2026-05-04 | ✅ | 2d | 2026-05-06 | Plan #4 #2。max-heap of size k pattern 一次寫對；`(-dis, i)` 用 idx 當 tie-breaker（避免比 list）細節到位。Gap：(1) 沒主動講「為什麼 max-heap 不是 min-heap」的直覺 (2) 不知道 quickselect 名稱 (3) sqrt 跳過的數學依據（monotonic + 非負）講得太籠統。SR 重做時要能口頭講出這 3 點。可考慮優化用 `heappushpop`（push+pop 合併為 1 次 sift） |
| 207 | Course Schedule | M | Graph / Topological Sort | 2026-05-04 | ✅ | 2d | 2026-05-06 | Plan #4 #3。首次接觸 Kahn's algorithm，自己推導出 in-degree + BFS 的核心邏輯。Code 第一版冗餘：(1) `visited` set 多餘（Kahn's in-degree 機制本身保證 node 最多 push 一次）(2) BFS-by-level 結構（外 while + 內 for range(len(q))）也多餘，topo sort 不分 level。複雜度寫 O(E) 漏算 V，正解 O(V+E)。**DFS-based cycle detection (3-color/3-state) 完全沒接觸過** → ANALYSIS P1 #7。SR 重做要點：(1) 直接寫簡化版（無 visited、無 level loop）(2) 改用 DFS 解法（white/gray/black 偵測 back edge）(3) Edge direction 為什麼是 prereq → dependent 要能口頭講 |
| 300 | Longest Increasing Subsequence | M | DP / Binary Search | 2026-05-05 | ⚠️ | 2d | 2026-05-07 | Plan #4 #4。10 min 完成 DP + BS 兩版。**DP 卡點**：dp[i] 定義初版模糊（「當前最長」未錨定 ending at i），需多輪引導才寫出「以 nums[i] 結尾的 LIS 長度」+ 最終答案是 max(dp) 不是 dp[-1]。**BS 全新 pattern**：初次方向誤判為 mono stack，用 [0,1,0,3,2,3] 反例破解；tails 演算法 + invariant 從零教學。**思路 3 段需多次精確化**：tails[k] 精確定義（長度 k+1 子序列的最小結尾）、為何 tails 嚴格遞增（砍結尾論證）、為何覆寫安全（長度不變 + 未來潛力大），初版用「紀錄最大長度 list」帶過。Code 細節對：bisect_left（strictly increasing 用左界）、append vs 覆寫分支。SR 重做要點：(1) 口述精確 tails[k] 定義（含「長度」+「最小結尾」兩 keyword）(2) 結構性論證 tails 遞增（砍結尾）(3) 覆寫安全雙段論證 (4) 為何 bisect_left 不是 bisect_right (5) 跳過 trace 直接 code 的習慣要改 |
| 124 | Binary Tree Maximum Path Sum | H | Tree / Recursion | 2026-05-05 | ⚠️ | 2d | 2026-05-07 | Plan #4 #5（wildcard Hard）。10 min 完成，遠超 < 40 min Hard 目標。Code 一次過 7 cases。**核心 insight 對**：分開維護「回傳值=一條腿」與「全局 max=兩條腿在 node 折返」+ 用 `max(腿, 0)` 處理負腿。**Q-A/B 不對稱口述對**：「全局可折返用兩腿；回傳要讓 parent 線性接只能一腿」。**Q-D self vs tuple** 選 self，理由「明確標記跨節點累積，不混淆」具體到位。**問題 1：思路書寫與 code 不符**（初版寫「return [max, ...]」但 code 用 self. 維護），不對稱原因只在 chat 講清楚未落到檔案。**問題 2：Code 雖正確但繁瑣**：第一版 `max(self.tmpMax, resL+v+resR, v, v+resL, v+resR)` 列 4 候選；改版 `max(0, resL+resR, resL, resR)` 仍列 4 case。最乾淨應為「個別淨化腿」：`gainL=max(resL,0); gainR=max(resR,0); v+gainL+gainR`，意圖更直白。**問題 3：沒主動 clarifying**，是被列點問才答。SR 重做要點：(1) 用「個別淨化腿」寫法 (2) 思路寫進「不對稱」原因 (3) 主動問 clarifying（單節點、負值、不過 root）(4) 口述「split at node = 兩腿折返」這個 insight |
| 33 | Search in Rotated Sorted Array | M | Binary Search | 2026-05-08 | ⚠️⚠️ | 2d | 2026-05-10 | Plan #5 #2。結構觀察（rotated = sorted+sorted、對半切必有一半 sorted）+ 用 `nums[m]` vs `nums[r]` 判斷哪半 sorted + Template A（`while l<=r` 找 exact target）都對。**雙重邊界 bug**：(1) 第一版兩處外側邊界寫 strict `<` 漏 target=nums[l]/nums[r] case，預填 test 故意不蓋邊界讓 "All tests passed!" 變假象 (2) 過修把指標 `m+1`/`m-1` 改成 `m` → infinite loop。**核心矯正**：外側邊界（`nums[l]`/`nums[r]`）必須 `<=`（值未被排除）；指標移動必須 `m±1`（`nums[m]` 已 return 排除，且不跳過會 infinite loop on `r=l+1`）。**根本弱項：trace 紀律** —— 兩次明確要求紙筆 trace `target=2`/`target=4` 都未做，學生誠實承認。SR 重做要點：(1) **動 code 前先紙筆 trace 邊界 case**（target=nums[l]、target=nums[r]、target 不在範圍） (2) 區分「值比較邊界」vs「指標移動邊界」是兩件事 (3) 思路要寫進這個區分 (4) test 要主動補邊界 case，不要等別人提醒。**已預定 LC 153（同 rotated 結構、找 pivot）作為下次紀律重做題** |
| 322 | Coin Change | M | DP / Unbounded Knapsack | 2026-05-09 | ✅ | 2d | 2026-05-11 | Plan #5 #3。首次 unbounded knapsack。Code 一次過 5 cases（含 `[186,419,83,408],6249→20` greedy-fail edge）。**思路初版偏薄（同 #2 弱項）**，二版補完 4 段：base case 語意（「amount=0 by definition」非反推 example 3）+ sentinel `float('inf')` 選擇（不可被合法解超過，min() 永遠取到合法解；最終 `dp[amount]==inf` 表示湊不出來→-1）+ `dp[i-coin]+1` 的「上一步加一枚」semantic + min 角色。**Trace 紀律先偷懶**（只 trace `[2],3` sub-case），被點名後補 `[1,2,5],5` 三層 trace（coin=1 跑完→[0,1,2,3,4,5]；coin=2 跑完→[0,1,1,2,2,3]；coin=5 跑完→[0,1,1,2,2,1]）正確。Loop order 選 outer coins / inner amount（**對 322 兩者等價，但 LC 518 combinations 會差** — 外 coins/內 amount 算組合，反過來算 permutations，已記彩蛋）。`range(coin, amount+1)` 對：避免 negative index silent bug（Python 負 index 繞回尾巴）+ 省 loop。**FU1 reconstruction**：第一直覺「dp[i] 存 list」可行但 O(A²/min_coin) space；引導到 parent pointer pattern `dp[i]=(count, last_coin)` → O(A) extra（72/1143 通用）。**FU2 BFS framing**：誤想 Dijkstra（uniform weight 不需 PQ），「BFS space 多」分析錯（加 visited 後同級）；BFS 早停在「amount 大、最佳解小」時優於 DP（具象例：amount=10000、coins=[1,5,100,2500]、最佳=4 → 只展 4 levels；DP 仍要算 10001 cells）。**SR 重做要點**：(1) 思路一開口就 4 段（base/sentinel/recurrence/min 角色）不需引導 (2) base case 從定義推非從 example 反推 (3) 322 vs 518 loop order 差別要記 (4) reconstruction 直覺直接是 parent pointer 不是 store list (5) trace 紀律：寫前要主動對 example 1 trace dp 演進 |
| 76 | Minimum Window Substring | H | Sliding Window | 2026-05-13 | ✅ | 2d | 2026-05-15 | Plan #5 #5。首次 sliding window Hard pattern。Code 一次過 6 cases（含 duplicates、tricky shrink edge），~35 min（達 Hard <40 min 目標）。**進步點**：(1) **clarifying 主動**（`m vs n` early return、case sensitive）——#560 後第二次穩定 (2) **`==`/`<` 邊緣偵測對稱性**寫對（increment `==`、decrement `<`，這題最易錯細節避開）(3) **trace 寫進 code comment**（line 82-89），紀律延續 #322/#560 (4) **Code review 兩 Socratic 點自己改對**：`need = defaultdict(int)` → `{}` + `c in need` guard（避免 pollute；`curr` 留 defaultdict 因要追所有 s 字元）；`if valid != needLen: continue` 與 `while` 冗餘 → 拿掉 continue。**思路升級**：1 段 → 3 段（演算法骨架 + `[l,r]` vs slice 微優化 + `valid` counter 為何存在）。**仍缺**：**monotonicity** 段（「擴大保 valid、縮小保 invalid」雙向單調 → 為什麼 sliding window 成立）。**FU1 多最短 window**：兩 ans 結構（list + ansLen），新 min 清空、等 min append ✓；**FU2 stream**：r/l 單向 → online algorithm ✓；**FU3 10^9 scale**：O(n+m) 漸進最佳 ✓，但漏 array[128] 取代 hashmap 的 constant factor 改進（C++/Rust 必選）。**edge case `t="aa"` 對 `==` vs `>=`**：r=0 curr=1≠2，r=1 curr=2==2 才觸發——「edge detection」非「state check」直覺到位。**SR 重做要點**：(1) 思路一開口要 4 段（含 monotonicity）(2) 主動講 array[128] 優化作為 const-factor 補充 (3) 主動 clarifying + trace 紀律繼續保持 (4) 寫前先口述 invariant：window valid ⟺ formed == need |
| 153 | Find Minimum in Rotated Sorted Array | M | Binary Search | 2026-05-19 | ✅ | 2d | 2026-05-21 | Plan #6 #1。**#33 紀律重做題**——成功修復。Template B + `nums[m]` vs `nums[r]` 一次過 6 cases。兩 trace case 主動執行寫進 code comment（#33 抗拒 trace 的弱項已修復）。思路兩分支 + `nums[l]` 反例（`[1,2,3]` 切錯邊）正確。**Gap**：未講 Template B invariant（`r=m` 不 infinite loop 因 `m<r` 必縮小）；Q2 初版「確認那邊有排序」太淺，靠追問補論證。**SR 重做要點**：(1) 開口先講 invariant（答案永遠在 `[l,r]`，`l==r` 即答案）(2) 主動論證 `r=m` 為何不 infinite loop (3) 為什麼用 `nums[r]` 不用 `nums[l]` 要直接給反例 (4) trace 紀律繼續保持 |
| 560 | Subarray Sum Equals K | M | Hash Map / Prefix Sum | 2026-05-10 | ⚠️ | 2d | 2026-05-12 | Plan #5 #4。首次 prefix sum + hashmap 經典 pattern。Code 一次過 7 cases（含 `[0,0,0],k=0→6`、`[1,-1,0],k=0→3`、含負數）。**進步點**：(1) **主動問 clarifying「array 是 sorted 嗎」**——#33/#322 沒做到，本次 Google 面試本能浮現 (2) **主動 trace `[1,1,1],k=2`**（hashmap 演進 + count 累加）不需被點名，紀律比 #33/#322 進步。**Misconception**：sliding window 適用條件第一直覺講「sorted」，正解是「**所有元素 ≥ 0**」（用 sorted-with-negatives 反例 `[-3,-1,2,5]` 破解 → prefix sum 非單調，expand/shrink 邏輯崩）。**Q4 prefix 等式 `sum(nums[i..j]) = prefix[j+1] - prefix[i]` 對**；Q5 lookup `P_curr - k` 需要 nudge 才寫精準。**Q6 因果倒了**：init `{0:1}` 寫對但解釋成「nums[0]..nums[j] 全選」（這是效果），正解是「**空 prefix（0 個元素和=0）的預設狀態存在 1 次**」（這是原因）→ 用對但沒真懂。**Code 可優化（未做到）**：用了 `prefix=[0]*(n+1)` array 存全部前綴，但只需單一 int 即可（過去 prefix 已由 hashmap 記住）→ canonical 解法是 `seen={0:1}; cur=0; for x in nums: cur+=x; res+=seen[cur-k]; seen[cur]+=1`，extra space O(1) 不算 hashmap。**思路仍偏薄**：一句話帶過，沒分 4 段（base/hashmap 內容/lookup 公式/為何不需 prefix array）。**SR 重做要點**：(1) sliding window 條件講「非負」不是「sorted」 (2) 開口直接用 single-int 版本，不要再開 prefix array (3) `{0:1}` 解釋「empty prefix 預設」不是「全選」 (4) 思路 4 段書面化 (5) 主動 trace + 主動 clarifying 的好習慣繼續保持 |

## Mastered（通過 32d 複習後結業）

| # | 題目 | 結業日期 | 總複習次數 |
|---|------|----------|-----------|
| — | — | — | — |

---

## Update Protocol

每次 `/practice` 完成該題時由 skill 依此表更新：

| 本次結果 | 動作 |
|----------|------|
| ✅ **clean solve**（無提示 + 時間達標）| 進下一階段：2d → 7d → 16d → 32d；若從 32d 通過 → 移到 Mastered |
| ⚠️ **需要提示** 或 **超時** 或 **次優解** | 維持當前階段，`下次日期 = 今天 + 階段天數` |
| ❌ **無法解出** | 重置到 2d，`下次日期 = 今天 + 2` |

**時間達標標準**（複習版，比首解嚴格）：
- Medium 複習目標：< 15 min
- Hard 複習目標：< 25 min

---

## 排程納入規則

`/practice` 完成**新題**時自動判斷是否加入 Active：

| 情況 | 是否排程 |
|------|----------|
| ⚠️ 或 ❌ 結果 | ✅ 必加 |
| Hard 難度 ✅ | ✅ 必加（高保留成本） |
| 新主題首次 ✅（ANALYSIS 弱項/缺口 section 的主題，或首次接觸的 pattern） | ✅ 必加（鎖定新概念） |
| 熟練主題的 Medium/Easy ✅ | ❌ 不加（低 ROI） |

---

## 與 /study 的整合

`/study` 生成 5 題計畫時：
- **「1 題 review」槽位**優先從 Active 中 `下次日期 ≤ 今天` 的項目選一個（取最久未複習的 = 下次日期最早的）
- 複習題以**原題**出現在計畫中（SR 機制就是重做原題，不換題）
- 若當天無 due 項目 → 退回 Stage 1 fallback：從歷史 ⚠️ 題目找同主題變體題
