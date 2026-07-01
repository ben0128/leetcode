# Quickselect / Partition

## 什麼時候用
- 找第 k 小/大的元素，或前 k 個最小/最大，但**不需要整個陣列排序好**
- 例如：Kth Largest Element、K Closest Points to Origin、Top K Frequent Elements
- 目標平均複雜度 O(n)，比完整排序的 O(n log n) 快

## 核心概念：Partition（來自 quicksort）
選一個 pivot，重新排列陣列讓「≤ pivot 都在左邊、≥ pivot 都在右邊」，pivot 最終落在它**排序後會在的位置**——即使左右兩邊個別都還沒排序。

## 模板（Lomuto partition scheme）

```python
def partition(arr, lo, hi):
    pivot = arr[hi]            # 選最後一個當 pivot（隨機選可避免 worst case）
    i = lo                     # i = 「≤pivot 區域」的右邊界
    for j in range(lo, hi):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[hi] = arr[hi], arr[i]   # 把 pivot 換到它最終的位置
    return i                   # pivot 的最終 index
```

## Quickselect：只往一邊遞迴

```python
def quickselect(arr, lo, hi, k):   # 找「排序後 index=k」的元素
    if lo == hi:
        return arr[lo]
    p = partition(arr, lo, hi)
    if p == k:
        return arr[p]
    elif p < k:
        return quickselect(arr, p + 1, hi, k)
    else:
        return quickselect(arr, lo, p - 1, k)
```

跟 quicksort 的差別：quicksort 兩邊都遞迴（T(n) = 2T(n/2) + O(n) → O(n log n)）；quickselect 只選一邊繼續，另一邊直接丟棄不管，所以是 T(n) = T(n/2) + O(n) → n + n/2 + n/4 + ... = O(n)。

## 複習時問自己這些問題

### 1. Partition 完之後，能保證什麼？
Pivot 左邊的元素都 ≤ pivot、右邊都 ≥ pivot，且 pivot 落在它排序後最終會在的 index。但左右兩邊個別**不保證排序好**。

### 2. 為什麼 quickselect 平均是 O(n) 而不是 O(n log n)？
Quicksort 每層遞迴兩邊都要處理。Quickselect 每次 partition 完只需要往其中一邊繼續（另一邊已確定不含答案，直接丟棄），呈等比級數 n + n/2 + n/4 + ... = O(2n) = O(n)。

### 3. Worst case 是什麼？怎麼避免？
如果每次選到的 pivot 都是當前範圍的最大或最小值（例如陣列已排序、每次選最後一個當 pivot），partition 完全不平衡 → O(n²)。
避免方式：**隨機選 pivot**（或 median-of-three），讓 worst case 機率極低。

### 4. K Closest Points to Origin 怎麼套用？
不直接排序座標，而是拿「與原點的距離平方」當比較 key 做 partition。目標讓某個 index 左邊的 k 個點就是距離最小的 k 個點——不需要這 k 個點彼此之間有序。

## 適用題目
| 題目 | 重點 |
|------|------|
| 215. Kth Largest Element in an Array | 最經典的 quickselect 應用 |
| 973. K Closest Points to Origin | 用距離平方當 key，不用 sqrt |
| 347. Top K Frequent Elements | 用出現次數當 key |
