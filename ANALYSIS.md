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
| Stack / Monotonic Stack | 8+ | ✅✅ | — | proficient | daily-temperatures、largest-rectangle 穩定 |
| Binary Search | 8+ | ✅✅ | — | proficient | 覆蓋完整 |
| Trees (general) | 18+ | ⚠️⚠️ | 2d | **weak** | iterative inorder 首次接觸（94 ⚠️） |
| BST | 3 | ⚠️✅ | 2d | **weak** | 230 Kth ⚠️；歷史 LCA 沒用 BST 性質 O(h) |
| Backtracking | 12+ | ✅✅ | — | proficient | subsets/permutations/combinations 全覆蓋 |
| Graph BFS/DFS | 14+ | ✅✅ | — | proficient | — |
| Union Find | 2 | ⚠️✅ | 2d | **weak** | 題數<3；count-connected 歷史 11 次；547 ✅ 剛鞏固 |
| DP (1D) | 5 | ⚠️— | — | **weak** | house-robber 8 次，直覺未自動化 |
| DP (2D) | 1 | ⚠️— | 2d | **weak** | 題數<3；97 首次接觸需引導 |
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
