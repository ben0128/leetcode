# DFS 拓撲排序 + 3-Color Cycle Detection（210 Course Schedule II 首次接觸）

> 建立日：2026-05-29，由 210 Course Schedule II 而生（#207 用過 Kahn's BFS，這次強制練 DFS 版）
> 包含：3-color DFS、為什麼 post-order + reverse 才對（pre-order 會壞）、模板、Kahn's vs DFS 對比

---

## Part 1：Edge 方向決定一切

`prerequisites[i] = [a, b]` 表示「**先修 b 才能修 a**」。建圖前先想清楚邊指哪：

- **慣例（本筆記採用）**：edge **prereq → dependent**，即 `b → a`。`graph[b].append(a)`
- 拓撲序要的是 **prereq 排在 dependent 前面**

> ⚠️ **edge 方向 ↔ 要不要 reverse 是綁死的**。選錯一個，答案順序就反掉。
> - edge = prereq→dependent + post-order append + **reverse** ✓
> - edge = dependent→prereq + post-order append + **不 reverse** ✓
> 不要兩個都選或都不選。建圖時先把方向定死，再決定 reverse。

---

## Part 2：3-Color（白/灰/黑）狀態 = Invariant

用一個 `colors` array（size = numCourses）記三種**狀態**（不是步驟）：

| 顏色 | 值 | 狀態意義（invariant） |
|------|-----|----------------------|
| ⚪ 白 | 0 | 還沒訪問 |
| 🟡 灰 | 1 | **正在當前這條 DFS 路徑上**（已進入、子孫還在探索中） |
| ⚫ 黑 | -1 | **完全處理完**（子孫全部走完、已 append），安全可剪枝 |

### Cycle detection 的核心

- DFS 中**碰到灰色** = back edge = 走回了當前路徑上的祖先 → **有環** → return `[]`
- 碰到**黑色** = 這個點之前已證明安全，直接跳過（剪枝），**不是** cycle

**為什麼一定要分灰/黑兩種，不能合併成「visited」？**
若只有一個 visited 旗標，你無法區分「碰到的是當前路徑上的祖先（真環）」還是「碰到之前別條分支處理完的點（無害的 cross/forward edge）」。把兩者都當環 → false positive；都不當環 → 漏掉真環。**灰 vs 黑 = 環偵測的全部意義。**

---

## Part 3：🔴 為什麼是 post-order + reverse，不是 pre-order 直接 return？

這是這題最容易「會寫但講不出」的點。

### 一句話

- **變黑（finish）的定義** = 「我指向的所有點都處理完、都 append 了」。所以一個 prereq **一定比它所有 dependent 都晚變黑** → answer 裡 dependent 全排在 prereq 前面 → reverse 一翻，prereq 全跑到 dependent 前面 = 正確拓撲序。**結構保證、免費得到。**
- **變灰（discover）沒有任何這種保證**。你剛踏進一個點時，不知道「別的分支上還有沒有東西也該排在它前面」。

### 反例：pre-order 會壞（一條鏈看不出來，要用「兩 prereq 指同一點」）

> 先修 0 才能修 2、先修 1 才能修 2。
> edges（prereq→dependent）：`0→2`、`1→2`　→　`graph = {0:[2], 1:[2], 2:[]}`
> 合法答案必須讓 **2 排最後**（如 `[0,1,2]` / `[1,0,2]`）

**pre-order（變灰就 append）**，外層 loop 0→1→2：
```
DFS(0): append 0 → [0]
  → DFS(2): append 2 → [0, 2]   ← 2 在這裡就被定死
DFS(1): append 1 → [0, 2, 1]    ← 1 是 2 的 prereq 卻排在 2 後面 ✗
結果 [0, 2, 1]：2 跑到 1 前面，違反「先 1 再 2」
```

**post-order（變黑才 append）+ reverse**：
```
DFS(0): 灰0
  → DFS(2): 灰2 → 無鄰居 → 黑2, append 2 → [2]
  黑0, append 0 → [2, 0]
DFS(1): 灰1 → 鄰居2已黑跳過 → 黑1, append 1 → [2, 0, 1]
reverse → [1, 0, 2] ✓
```

**記憶句**：⚫黑色 = 「下游全部搞定」的保證；🟡灰色只是「我剛到」。拓撲序要的是「下游先就位」，所以只能在變黑那一刻記錄，最後再反轉。

---

## Part 4：模板（DFS 版）

```python
def findOrder(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    for a, b in prerequisites:        # 先修 b 才能修 a
        graph[b].append(a)            # edge: prereq → dependent

    colors = [0] * numCourses         # 0=白 1=灰 -1=黑
    order = []

    def dfs(node):
        colors[node] = 1              # 進入 → 灰
        for nxt in graph[node]:
            if colors[nxt] == 1:      # 碰到灰 → 環
                return False
            if colors[nxt] == 0 and not dfs(nxt):
                return False          # 黑(-1)直接跳過（剪枝）
        colors[node] = -1             # 子孫全完 → 黑
        order.append(node)            # post-order append
        return True

    for i in range(numCourses):       # ← 外層 loop：圖可能不連通/多根
        if colors[i] == 0:
            if not dfs(i):
                return []             # 有環
    return order[::-1]                # reverse
```

要點：
- **外層 loop 必須有**：圖可能有多個不相連的部分或多個入度 0 的根，不能只從某個點起。
- 黑色（-1）node 在迴圈裡是「跳過」，不是回傳 False。只有灰色才是環。
- `order` 在變黑時 append，最後 `[::-1]`。

**複雜度**：Time `O(V + E)`（每點每邊各訪一次）；Space `O(V + E)`（adjacency list `O(V+E)` + colors `O(V)` + recursion stack `O(V)`）。

---

## Part 5：DFS 版 vs Kahn's BFS 版

| | **DFS（3-color）** | **Kahn's（BFS）** |
|---|---|---|
| 核心 | post-order + reverse | in-degree=0 入 queue，逐個移除 |
| 環偵測 | 碰到灰色（back edge） | 最後 `len(order) != numCourses` |
| 拓撲序產生 | 變黑 append → reverse | pop 出 queue 的順序即是 |
| 額外結構 | colors array + recursion stack | in-degree array + queue |
| 遞迴 | 是（深圖小心爆 stack，可改顯式 stack） | 否（純迭代） |

面試 follow-up 常見：「你用了 BFS，能用遞迴/DFS 寫嗎？」或反過來。**兩個方向都要會。**

---

## 複習時問自己

1. `prerequisites=[a,b]` 我的 edge 指哪邊？（prereq→dependent）為什麼這樣選 → 配 reverse？
2. 灰色、黑色各代表什麼**狀態**（不是步驟）？碰到灰色 vs 黑色分別代表什麼？
3. 為什麼不能把灰/黑合併成一個 visited？（答：分不出真環 vs 無害 cross edge）
4. 為什麼是「變黑才 append + reverse」而不是「變灰就 append」？（答：黑色保證下游全部就位；用 `0→2`、`1→2` 反例說明 pre-order 壞掉）
5. 外層 loop 為什麼必要？（答：圖可能不連通 / 多根）
6. 複雜度 Time / Space？成本來源各是什麼？

## 常踩坑

| 坑 | 症狀 | 修法 |
|----|------|------|
| edge 方向與 reverse 不一致 | 答案順序整個反掉 | 建圖前定死方向，prereq→dependent 配 reverse |
| 灰/黑不分（只用 visited） | 漏判環 或 誤判環 | 三色：灰=路徑上、黑=已完成 |
| 變灰就 append | 多 prereq 指同一點時順序錯 | post-order：變黑才 append |
| 忘記 reverse | 順序剛好反 | `order[::-1]` |
| 漏外層 loop | 不連通/多根的圖漏節點 | `for i in range(n): if white: dfs(i)` |
| 黑色 node 回傳 False | 把已完成點誤當環 | 只有灰色才是環，黑色 = 跳過 |

## 適用題目

| 題目 | 特徵 | 備註 |
|------|------|------|
| 207 Course Schedule | 只問能不能修完（bool） | DFS 環偵測 / Kahn's 都可 |
| 210 Course Schedule II | 回傳一個合法順序 | 本筆記主題 |
| 269 Alien Dictionary | 從字典序建圖 + 拓撲排序 | 建圖較難，排序同模板 |
| 310 Minimum Height Trees | 從葉子往內剝（類 Kahn's） | 無向圖變體 |
| 802 Find Eventual Safe States | 反向圖 + 環偵測 | 3-color 經典應用 |
| 1136 Parallel Courses | 拓撲排序求最少學期數 | Kahn's 分層 |
