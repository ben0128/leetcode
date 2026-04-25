# Binary Search 兩種 Template 完全指南

> **核心痛點**：`while l < r` 還是 `while l <= r`？`r = mid` 還是 `r = mid - 1`？這兩個選擇看起來很像，但搞錯就會陷入 infinite loop 或 off-by-one。
>
> **這份筆記目的**：建立一個**判斷規則**，讓你看到 BS 題能在 30 秒內決定該用哪個 template。

---

## 一句話判斷規則

| 我在找什麼 | 答案保證存在嗎 | 用哪個 |
|------------|-----------------|--------|
| 一個**位置**（最小/最大滿足條件的 index） | ✅ invariant 保證 | **Template A** |
| 一個**確切的值** | ❌ 可能不存在 | **Template B** |

簡記：**A = "answer is somewhere in [l, r]"**, **B = "compare and narrow"**。

---

## Template A：`while l < r`（找位置，invariant 保證存在）

### 骨架

```python
def template_a(nums):
    l, r = 0, len(nums) - 1
    while l < r:                    # 注意：嚴格小於
        mid = l + (r - l) // 2
        if condition(nums[mid]):    # mid 滿足條件
            r = mid                 # ← 不是 mid - 1！mid 可能就是答案
        else:
            l = mid + 1             # mid 不滿足 → 跳過 mid
    return l                        # 最後 l == r，回傳 l
```

### 為什麼 work？

**Invariant**：「答案永遠在 `[l, r]` 範圍內」。每次迭代後這個 invariant 不被破壞，且範圍嚴格縮小，最後 `l == r` 就是答案。

### 為什麼用 `r = mid` 而不是 `r = mid - 1`？

因為 `mid` 自己**可能就是答案**。例如「找第一個 True」：

```
[F, F, F, T, T, T]
       ↑
      mid=2, condition(F)=不滿足 → l = mid + 1 = 3
[F, F, F, T, T, T]
          ↑
         mid=3, condition(T)=滿足 → r = mid = 3 (不能 mid-1，否則會跳過正確答案)
l == r == 3, return 3 ✓
```

### 經典題型

| LC# | 題目 | condition |
|-----|------|-----------|
| 162 | Find Peak Element | `nums[mid] < nums[mid+1]` (升 → 排掉左半) |
| 278 | First Bad Version | `isBadVersion(mid)` (排掉左半) |
| 35 | Search Insert Position | `nums[mid] >= target` |
| 153 | Find Min in Rotated | `nums[mid] > nums[r]` (排掉左半) |
| 875 | Koko Eating Bananas | `canFinish(mid)` (二分速度) |
| 1011 | Capacity To Ship | `canShip(mid)` (二分容量) |

→ **找位置題幾乎都用 A**

---

## Template B：`while l <= r`（找值，可能不存在）

### 骨架

```python
def template_b(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:                   # 注意：等於也要進
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid              # 找到 → 直接回傳
        elif nums[mid] < target:
            l = mid + 1             # ← 必須 mid + 1（mid 已比較過）
        else:
            r = mid - 1             # ← 必須 mid - 1（mid 已比較過）
    return -1                       # 沒找到
```

### 為什麼 work？

**Invariant**：「target 如果存在，一定還在 `[l, r]` 之內」。當 `l > r` 時範圍變空，代表沒找到。

### 為什麼用 `mid - 1` / `mid + 1` 而不是 `mid`？

因為 `mid` 已經比較過了（不是 target），下次不該再比一次。如果寫 `r = mid` 會 infinite loop（範圍永遠卡著不縮小）。

### 經典題型

| LC# | 題目 | 備註 |
|-----|------|------|
| 704 | Binary Search | 教科書版 |
| 33 | Search in Rotated Sorted Array | B 的進階：先判斷哪一半有序，再用 B 邏輯 |
| 74 | Search a 2D Matrix | 把 2D 視為 1D 後跑 B |

→ **找值題用 B**

---

## 兩個容易混淆的對照

### 對照 1：`r` 初始值

| Template | `r` 初始 |
|----------|---------|
| A | `len(nums) - 1`（一般情況）或 `len(nums)`（找 insert 位置時可越界） |
| B | `len(nums) - 1`（永遠在合法 index 內） |

### 對照 2：迴圈結束條件 vs 更新

```
Template A：
  while l < r          # 嚴格 < 才進
  r = mid              # 不減 1（保留候選）
  l = mid + 1          # 加 1（排除 mid）

Template B：
  while l <= r         # <= 才進
  r = mid - 1          # 減 1（mid 已比過）
  l = mid + 1          # 加 1（mid 已比過）
```

**記憶口訣**：
- A 是「**保留中間**」（mid 可能是答案，所以 `r = mid` 不切掉它）
- B 是「**排除中間**」（mid 已比過不是 target，所以 `r = mid - 1` 切掉）

---

## 三步快速判斷（看到 BS 題就跑這個 checklist）

1. **我在找什麼？**
   - 找 target 值（`==` 比較）→ 直接 B
   - 找邊界位置（「最小/最大滿足 X 的 index」、「peak」、「首個 True」）→ 通常 A

2. **答案是否保證存在？**
   - 是（invariant 保證）→ A，最後 return `l`
   - 否（可能找不到）→ B，最後 return `-1`

3. **mid 自己有可能是答案嗎？**
   - 是 → A，更新時 `r = mid`（不切掉）
   - 否（mid 就是 target，已 return；或不是 target 才 narrow）→ B，更新時 `r = mid - 1`

---

## ⚠️ Equality 殺手（BS 死亡情境）

當「比較結果無法決定丟哪半」時，BS 直接退化 O(n)。

### 案例：162 Find Peak Element 拿掉 `nums[i] != nums[i+1]` 的 constraint

| 比較 | 能推 peak 在哪？ |
|------|------|
| `nums[mid] < nums[mid+1]` | 右半 ✓ |
| `nums[mid] > nums[mid+1]` | 左半 ✓ |
| `nums[mid] == nums[mid+1]` | **不知道**（兩邊都可能） |

**反例**：
- `[9, 1, 3, 3, 1, 1]` 與 `[1, 1, 3, 3, 1, 9]` 在 mid=2、mid+1=3 看到的都是 `3 == 3`，但 peak 一個在左半一個在右半 → BS 沒辦法用一次比較決定。

### 同樣 pattern 的題

- LC 81 Search in Rotated Sorted Array II（允許重複）→ 最壞 O(n)
- LC 154 Find Min in Rotated Sorted Array II → 最壞 O(n)
- LC 162（拿掉 `!=` constraint）→ 最壞 O(n)

**面試標準答案**：「在原 constraint 下 BS 可解 O(log n)；放寬 constraint 後 worst case O(n)，因為 equality 破壞 invariant，無法保證每步丟一半安全」。

---

## 常見 Off-by-One 陷阱

| 寫法 | 結果 |
|------|------|
| Template A 寫成 `while l <= r` + `r = mid` | **Infinite loop**（l == r 時還進迴圈，且 r 不變） |
| Template A 寫成 `r = mid - 1` | 可能跳過正確答案（mid 是答案時被切掉） |
| Template B 寫成 `r = mid` | **Infinite loop**（mid 已比過但 r 沒前進） |
| Template B 寫成 `while l < r` | 漏比最後一個 element（當 l == r 時） |

→ **記住對應關係**：
- `<` 配 `r = mid`
- `<=` 配 `r = mid - 1`
- 兩個對應**不能混搭**

---

## 練習路徑（建議順序）

1. **278 First Bad Version**（純 A，題目超直接）
2. **35 Search Insert Position**（A，但 r 初始是 `len(nums)` 而非 `len(nums)-1`，練越界處理）
3. **704 Binary Search**（純 B，教科書）
4. **162 Find Peak Element**（A 的進階：non-monotonic invariant）
5. **153 Find Min in Rotated**（A 的進階：跟 r 比而非跟 mid+1 比）
6. **33 Search in Rotated Sorted Array**（B 的進階：先判段哪半有序）
7. **875 Koko / 1011 Ship**（A 的應用：在「答案空間」二分而非陣列）

做完 1-3 應該就能穩定區分兩種 template。4-7 練 invariant 建立的能力。
