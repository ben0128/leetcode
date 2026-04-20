# BFS 模式總匯（127 Word Ladder 踩過的坑 + 變體）

> 建立日：2026-04-21，由 127 Word Ladder 綜合 learnings 而生
> 包含：BFS vs Dijkstra 決策、visited 標記時機、bidirectional BFS

---

## Part 1：何時用 BFS 而不是 Dijkstra？

### 核心判斷

**全部邊的「cost / distance」一樣** → 用 BFS（通常 cost = 1，即「一步」）
**邊的 cost 不一樣** → 用 Dijkstra（或 Bellman-Ford 若有負權）

| 問題特徵 | 正確演算法 |
|---------|-----------|
| 「最短路徑長度」+ 每步成本 = 1 | **BFS** |
| 「最短路徑長度」+ 每步成本不一 | **Dijkstra** |
| 「最少步驟 / 最少次操作」 | **BFS** |
| 「最少花費」+ 有 weight | **Dijkstra** |
| 「最短路 + 有負權」 | **Bellman-Ford / SPFA** |

### 127 的誤判

「相鄰 = 改一個字母」看起來像 graph 題，第一直覺可能跑到 Dijkstra。但**每一步成本都是 1**（不管是改哪個位置、哪個字母），所以 BFS 就夠了。

BFS 比 Dijkstra 好的地方：
- 不用 priority queue（少 `log` factor）
- 程式簡單（queue 即可）
- **Dijkstra 在無權重圖下會退化為 BFS，但常數慢**

### 面試警訊

說出 Dijkstra 時面試官會追問：「這題邊有權重嗎？」如果沒有，會期望你**主動降級到 BFS**。反過來若邊有 weight，不要用 BFS（可能錯或次優）。

---

## Part 2：Visited 標記時機（enqueue vs dequeue）

### Golden Rule

> **永遠在 enqueue 時 mark visited，不要等到 dequeue 時才 mark**

### 為什麼？

若在 dequeue 時才 mark visited：同一個 node 可能被**多個 parent** 同時 enqueue，造成 queue 膨脹。

### 錯誤 pattern（127 的原版）

```python
# ❌ pop 時才 check
while tmp:
    for _ in range(len(tmp)):
        popWord = tmp.popleft()
        if popWord in visited:      # ← 代表 queue 內有重複
            continue
        visited.add(popWord)        # ← 太晚 mark
        for candi in neighbors(popWord):
            if candi not in visited:
                tmp.append(candi)   # ← 沒 mark，同一個 candi 可能被別的 parent 再 append
```

**問題**：`hot` 可能同時是 `dot` 和 `lot` 的鄰居，兩個 parent 都把 `hot` enqueue → queue 裡有 2 個 `hot`，要等第 2 個 pop 時才被 `in visited` 擋掉。queue 大小膨脹。

### 正確 pattern

```python
# ✅ enqueue 時就 mark
visited = {beginWord}
tmp = deque([beginWord])

while tmp:
    for _ in range(len(tmp)):
        popWord = tmp.popleft()
        if popWord == endWord:
            return count
        for candi in neighbors(popWord):
            if candi not in visited:
                visited.add(candi)     # ← 進 queue 就 mark
                tmp.append(candi)
    count += 1
```

Queue 內**絕不會有重複**，pop 時不需要 `in visited` 的 check。

### 例外：什麼時候需要「pop 時 check」？

**幾乎沒有**。以下情況 enqueue-time mark 都適用：
- 普通 BFS
- Level-by-level BFS
- 01-BFS
- Multi-source BFS
- Bidirectional BFS

**真正需要 pop-time check 的是 Dijkstra**（因為 priority queue 可能有同一個 node 的不同 distance 版本，要取最先 pop 的那個），**不是 BFS**。

---

## Part 3：Bidirectional BFS（大 graph 的 optimization）

### Why 快？

分支因子 B、距離 d 時：
- 單向 BFS 要訪 **B^d** 個 node
- 雙向 BFS 兩邊各 **B^(d/2)** → 總共 **2·B^(d/2)**
- B=10, d=6：單向 10^6；雙向 2·10^3 → **快 500 倍**

### Memory 不是變多，是變**少**

**常見誤解**：「兩個 frontier、兩個 visited → 記憶體變 2 倍」
**真相**：frontier 本身的大小指數級縮小（從 B^d 降到 B^(d/2)），常數 2 倍完全被壓過去。

### 關鍵實作 point

1. **永遠從 frontier 較小的那一邊擴** — 這是**真正的 optimization**，遺漏這點就退化成普通 BFS
   ```python
   if len(frontierA) > len(frontierB):
       frontierA, frontierB = frontierB, frontierA   # swap，永遠擴小的
   ```
2. **Meeting detection**：擴展 A 邊新 node 時，check 該 node 是否在 B 邊的 visited → 若是 → 找到最短路
3. **算距離要小心 off-by-one**：兩邊各自計層數，相遇時 `return lenA + lenB + 1` 或 `lenA + lenB`（依你怎麼定義「遇到」的時機），這裡最容易 debug 到深夜

### 基本模板

```python
def bidirectional_bfs(start, end, wordList):
    if end not in wordList: return 0
    front = {start}
    back = {end}
    visited = {start, end}
    steps = 1

    while front and back:
        if len(front) > len(back):        # always expand smaller
            front, back = back, front

        next_front = set()
        for word in front:
            for neighbor in get_neighbors(word):
                if neighbor in back:       # meeting!
                    return steps + 1
                if neighbor not in visited:
                    visited.add(neighbor)
                    next_front.add(neighbor)
        front = next_front
        steps += 1

    return 0
```

### 什麼時候**不能**用 bidirectional BFS？

- 不知道終點是什麼（例如找「任一終點」或「最遠節點」）
- Graph 是 directed 且反向邊不知道
- 邊權重不一（這時要用 bidirectional Dijkstra，更複雜）

---

## 複習時問自己

1. 題目是「最短 / 最少步」且每步成本相同嗎？→ 如果是，寫 BFS 不寫 Dijkstra
2. 我 mark visited 的時機是 enqueue 還是 dequeue？**一定要 enqueue**
3. Queue 內有沒有可能有重複 node？若有 → 你做錯了
4. 如果題目改成「最少成本」且每步 cost 不同（例如 2-5-1），還可以用 BFS 嗎？（答：不行，需 Dijkstra 或 0-1 BFS）
5. Bidirectional BFS 的 memory 比單向**多**還是**少**？為什麼？（答：少，因 frontier 指數縮）
6. Bidirectional BFS 裡漏掉 "expand smaller" 會怎樣？（答：退化成近乎單向的效率，失去意義）

## 常踩坑（127 實戰）

| 坑 | 症狀 | 修法 |
|----|------|------|
| 用 Dijkstra | overengineer，多寫 priority queue | 改 BFS |
| pop 時才 mark visited | queue 膨脹，效率差 | enqueue 時 mark |
| 只在 `wordSet[wild]` 取得 candi 時 check visited | 仍有漏網之魚（別的 parent 會再 enqueue） | enqueue 前 `if candi not in visited: visited.add(candi); tmp.append(candi)` |
| Bidirectional BFS 固定輪流擴展 A/B | 退化成單向效率 | 每輪選 `len(frontier)` 較小的 |

## 適用題目

| 題目 | 特徵 | 技巧 |
|------|------|------|
| 127 Word Ladder | 每步 cost=1，單向 shortest | BFS；大 wordList 可 bi-BFS |
| 126 Word Ladder II | 同上但要 list all 最短路 | BFS 建層級 + DFS 回溯 |
| 200 Number of Islands | Connected components | BFS / DFS / UF 都可 |
| 994 Rotting Oranges | Multi-source BFS | 所有壞橘子一起當起點 |
| 1091 Shortest Path in Binary Matrix | 格子 BFS | BFS；可 A* 加速 |
| 752 Open the Lock | 每步改 1 位 | BFS 或 bi-BFS |
| 773 Sliding Puzzle | 每步交換 | BFS + state encoding |
| 815 Bus Routes | 每次上下車為一步 | BFS on routes（非 stations）|
