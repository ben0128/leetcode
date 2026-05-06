# Spaced Repetition Schedule

> **目的**：把做過的題目轉成長期記憶，避免「做過就忘」
> **依據**：Red-Green-Code doubling-interval 間隔重複；interleaving 研究（Rohrer & Taylor 2007）
> **機制**：首次解題後排程 2d → 7d → 16d → 32d → mastered
> **更新**：每次 `/practice` 完成複習後，skill 自動維護此檔

---

## Active（待複習）

| # | 題目 | 難度 | 主題 | 首次日期 | 首次結果 | 當前階段 | 下次日期 | 備註 |
|---|------|------|------|----------|----------|----------|----------|------|
| 94 | Binary Tree Inorder Traversal | M | Tree / Stack | 2026-04-12 | ⚠️ | 2d | 2026-04-14 | iterative inorder 首次 |
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
