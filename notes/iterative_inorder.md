# Iterative Inorder Traversal（用 stack 模擬遞迴）

## 什麼時候用
- 需要按照 BST 的排序順序處理 node
- 需要 early return（找到第 k 個就停），iterative 比 recursive 更直覺
- 面試官問「能不能不用遞迴？」

## 核心概念

遞迴的 inorder 是 `left → 自己 → right`，每次往左走就是把自己壓到 call stack。
Iterative 就是你自己管這個 stack，交替做兩件事：

**動作 A — 往左到底，沿途壓 stack**
**動作 B — Pop 出來處理，轉向右邊**

## 模板

```python
stack = []
curr = root
while curr or stack:
    while curr:             # 動作 A：一路往左到底
        stack.append(curr)
        curr = curr.left
    node = stack.pop()      # 動作 B：彈出來處理
    # --- 在這裡做你要做的事 ---
    curr = node.right       # 轉向右邊，回到動作 A
```

## 圖解

```
    5
   / \
  3   6
 / \
2   4

step 1: push 5, 3, 2       stack: [5, 3, 2]    curr = None
step 2: pop 2 → 處理        stack: [5, 3]       curr = 2.right = None
step 3: pop 3 → 處理        stack: [5]          curr = 3.right = 4
step 4: push 4              stack: [5, 4]       curr = None
step 5: pop 4 → 處理        stack: [5]          curr = 4.right = None
step 6: pop 5 → 處理        stack: []           curr = 5.right = 6
step 7: push 6              stack: [6]          curr = None
step 8: pop 6 → 處理        stack: []           curr = 6.right = None
→ curr = None, stack empty → 結束

處理順序: 2, 3, 4, 5, 6 ✓
```

## `while curr or stack` 的意思

| curr | stack | 意思 | 繼續？ |
|------|-------|------|--------|
| 有 | 任意 | 還有路可走 | ✓ |
| None | 非空 | 沒路了但還有未處理的 node | ✓ |
| None | 空 | 全部處理完了 | ✗ |

## 適用題目

| 題目 | 怎麼套模板 |
|------|-----------|
| 230. Kth Smallest Element in BST | `k -= 1; if k == 0: return node.val` |
| 94. Binary Tree Inorder Traversal | `result.append(node.val)` |
| 98. Validate BST | 檢查 `node.val > prev`，更新 `prev` |
| 173. BST Iterator | `next()` 就是執行一次動作 B，`hasNext()` 就是 `curr or stack` |

## 複雜度

- Time: O(n) — 每個 node 恰好 push 一次、pop 一次
- Space: O(h) — stack 最多放一條從 root 到 leaf 的路徑，h = 樹高
