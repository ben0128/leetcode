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
| 230 | Kth Smallest Element in BST | M | Tree / BST | 2026-04-12 | ⚠️ | 2d | 2026-04-14 | iterative inorder 應用 |
| 235 | Lowest Common Ancestor of BST | M | Tree / BST | 2026-04-11 | ✅ | 2d | 2026-04-13 | 修正舊解，改用 BST 性質 O(h) |
| 547 | Number of Provinces | M | Union Find | 2026-04-12 | ✅ | 2d | 2026-04-14 | UF template + path compression + rank |
| 97 | Interleaving String | M | 2D DP | 2026-04-13 | ⚠️ | 2d | 2026-04-15 | 第一次 2D DP，邊界需引導 |
| 295 | Find Median from Data Stream | H | Heap | 2026-04-13 | ✅ | 2d | 2026-04-15 | two-heap pattern |
| 239 | Sliding Window Maximum | H | Monotonic Queue | 2026-04-13 | ⚠️ | 2d | 2026-04-15 | 首次 monotonic queue，有兩個實作 bug |
| 64 | Minimum Path Sum | M | 2D DP | 2026-04-18 | ⚠️ | 2d | 2026-04-20 | 1D 滾動實作對但講不出「為什麼 work」；dp 定義/邊界/轉移需引導精準 |
| 236 | LCA of Binary Tree | M | Tree / Recursion | 2026-04-18 | ⚠️ | 2d | 2026-04-20 | 第一版 code 漏遞迴右子樹；post-order 與 inorder 措辭混淆；follow-up LL intersection 方向錯 |

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
