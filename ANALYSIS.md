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

### 強項（可以自信面對）

| 主題 | 題數 | 評估 |
|------|------|------|
| Array / Hashing | 30 | 大量練習，基本功扎實 |
| Two Pointers | 8 | 雖然掙扎多但最終解法都 optimal |
| Stack / Monotonic Stack | 8+ | daily-temperatures、largest-rectangle 都正確 |
| Binary Search | 8+ | 覆蓋完整 |
| Trees | 18+ | BFS/DFS/Inorder 模式穩定 |
| Backtracking | 12+ | 非常全面，subsets/permutations/combinations 全系列 |
| Graph BFS/DFS | 14+ | 基本 BFS/DFS 沒問題 |

### 弱項（需要重點加強）

| 主題 | 問題 | 建議 |
|------|------|------|
| **Dynamic Programming** | house-robber 花 8 次、partition-equal-subset-sum 花 5 次。DP 直覺不夠自動化 | 重點練 2D DP、Knapsack 變體、State Machine DP |
| **Union Find** | count-connected-components 花 11 次，是最大掙扎點 | 把 UF template 練到肌肉記憶，再做 3-5 題 UF |
| **BST 特性應用** | LCA 沒用 BST 性質 | 刻意練習利用 BST ordering 的題目 |
| **Heap 信心** | 基本 heap 題要 5-6 次 | 已改善但需要鞏固，建議練 merge k sorted |

### 缺口（完全沒練或極少）

| 主題 | 缺少的重要題目 | Google 出題頻率 |
|------|---------------|----------------|
| **Monotonic Queue** | sliding-window-maximum | 高 |
| **進階 DP** | distinct-subsequences, burst-balloons, regular-expression-matching, interleaving-strings | 中高 |
| **Segment Tree / BIT** | 零覆蓋 | 低但偶爾出現 |
| **進階 Design** | Iterator, Rate Limiter, LFU Cache | 中 |
| **Math** | 幾乎零覆蓋 | 低 |

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
