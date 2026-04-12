# Union Find Template

## 什麼時候用
- 判斷兩個 node 是否在同一個 connected component
- 計算有幾個 connected component
- 動態合併集合（不需要拆分）

## 模板

```python
roots = [i for i in range(n)]
ranks = [0 for _ in range(n)]      # rank = 邊數，不是 node 數，初始為 0

def find(node):
    while node != roots[node]:
        roots[node] = roots[roots[node]]  # path compression (path halving)
        node = roots[node]
    return node

def union(x, y):
    rootX, rootY = find(x), find(y)
    if rootX != rootY:
        if ranks[rootX] < ranks[rootY]:
            roots[rootX] = rootY
        elif ranks[rootX] > ranks[rootY]:
            roots[rootY] = rootX
        else:
            roots[rootY] = rootX
            ranks[rootX] += 1       # 只有等高時才 +1
```

## 複習時問自己這些問題

### 1. Rank 是什麼？為什麼初始值是 0？
- Rank 是從 root 到最深 leaf 的**邊數**（不是 node 數）
- 單一 node 沒有邊，所以初始值是 0

### 2. 為什麼矮的接到高的下面，rank 不用 +1？
```
rank=2       rank=1
  A            C         union 後 A 的高度沒變：
 / \                     A→D→C = 2 條邊，跟原本一樣
B   D          →         
                         rank=2
                           A
                          / \
                         B   D
                             |
                             C
```
矮樹接到高樹下面，最深路徑不會超過原本的最大高度。

### 3. 為什麼只有等高時才 +1？
```
rank=1    rank=1         兩邊一樣高，接上去一定多一層：
  A         C     →      rank=2
  |         |              A
  B         D             / \
                         B   C
                             |
                             D
```

### 4. 被合併的 node 需要更新 rank 嗎？
不需要。`find()` 永遠走到 root，只有 root 的 rank 會被讀取。非 root 的 rank 再也不會被用到。

### 5. Path compression 在幹嘛？
`roots[node] = roots[roots[node]]` 把 node 的 parent 指向 grandparent（path halving），每次 find 都壓扁樹，讓之後的 find 更快。

### 6. 有 path compression + union by rank，複雜度是多少？
- 單次 find/union: O(α(n)) ≈ O(1)（α 是 inverse Ackermann，實際上不超過 4）
- 整體：幾乎線性

## 適用題目

| 題目 | 重點 |
|------|------|
| 547. Number of Provinces | 基礎 UF，adjacency matrix，數 component |
| 323. Number of Connected Components | 同上，adjacency list |
| 684. Redundant Connection | 找出讓圖形成環的那條邊 |
| 721. Accounts Merge | UF + string 合併，較複雜的應用 |
| 128. Longest Consecutive Sequence | 可以用 UF 解（也可以用 set） |
