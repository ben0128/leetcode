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

## ⚠️ 常見陷阱：union 寫法寫錯會「斷鏈」

### 錯誤寫法（#721 **兩次**踩到：2026-05-01 首寫、2026-07-09 SR 重做原樣重演——做 UF 題前先重讀本節）

```python
roots[i] = find(j)        # ❌ 改的是「i 自己」的 parent
```

### 正確寫法

```python
roots[find(i)] = find(j)  # ✅ 改的是「i 的祖宗」的 parent
```

### 為什麼差這麼多？

當 `i` 已經被 union 過、有了 parent 之後：
- 錯誤寫法：把 `i` 自己的箭頭從舊 parent 改指到新 parent → **舊那條鏈直接斷掉**
- 正確寫法：找到 `i` 的祖宗，把祖宗的箭頭指到新 group → **整支家族一起搬，不斷鏈**

### ASCII 對照（i=2，先 union 到 0，再 union 到 1）

```
❌ roots[2] = find(...) 
   Step 1:   0          Step 2:    0       1
             ↑                              ↑
             2                      2   ← 跟 0 的連線消失
   
✅ roots[find(2)] = find(...)
   Step 1:   0          Step 2:     1
             ↑                       ↑
             2                       0   ← 0 的箭頭改指 1
                                     ↑
                                     2   ← 2 沒動，跟著上去

   結果：0、1、2 全部同一族
```

**口訣**：union 永遠搬「祖宗」，不要搬「自己」。所以 union 函式裡一定要先 `find` 兩邊。

---

## 進階模式：用 hash map 當「橋樑」

有時候要 union 的關係不是直接給的（不像 #547 給 adjacency matrix），而是要從題目的某個 attribute 推出來。這時候需要一個 hash map 當橋樑：

```python
attr_to_node = {}   # key = 共享的 attribute，value = 屬於哪個 node

for i in range(n):
    for attr in node_i_attrs:
        if attr in attr_to_node:
            union(i, attr_to_node[attr])   # 透過共享 attr 觸發 union
        attr_to_node[attr] = i
```

**典型例子**：
- #721 Accounts Merge：node = row index，attr = email
- #128 Longest Consecutive Sequence：node = 數字，attr = 相鄰數字（n-1, n+1）

**選 node 的原則**：選「天然唯一」的東西當 node（如 row index），用 attr map 找出該 union 誰。

## 適用題目

| 題目 | 重點 |
|------|------|
| 547. Number of Provinces | 基礎 UF，adjacency matrix，數 component |
| 323. Number of Connected Components | 同上，adjacency list |
| 684. Redundant Connection | 找出讓圖形成環的那條邊 |
| 721. Accounts Merge | row index 當 node，email map 當橋樑 |
| 128. Longest Consecutive Sequence | 可以用 UF 解（也可以用 set） |
