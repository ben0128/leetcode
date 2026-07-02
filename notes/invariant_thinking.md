# Invariant 思維（狀態，不是步驟）

## 什麼是 Invariant

**每一輪迴圈（或每層遞迴）開始時都成立的一句「事實描述」**。

- 它是**狀態**（「什麼永遠為真」），不是**步驟**（「我接下來做什麼」）
- 講出來的句子裡不應該有動詞「push / pop / 往左走」——那些是動作
- 判別法：把你的句子接在「不管迴圈跑到第幾輪，＿＿」後面，通不通順？

## 為什麼面試官在乎

Invariant 是**正確性的證明骨架**。演算法為什麼對、什麼時候能停、邊界為什麼這樣寫，全部從這句話推出來。講不出 invariant = 「code 會動但說不出為什麼對」→ Solution Design / Communication 掉分。

## 標準範例

| 演算法 | Invariant（狀態） | 從它推出什麼 |
|--------|------------------|-------------|
| Binary search | 「target 若存在，必在 `nums[lo..hi]` 內」 | 砍半安全性；`lo>hi` 可停（不存在） |
| #235 LCA of BST | 「p、q 永遠在**以 curr 為根的子樹**裡（**含 curr 本身**）」 | 單向下沉不用回頭；split 那刻 curr 即 LCA；split 條件要 `>=`（含等號接住 curr==p/q） |
| #239 Monotonic queue | 「deque 內 nums[index] 單調遞減 + 所有 index 都在 window 內」 | 隊首永遠是 window max |
| #64 Min Path Sum | 「站上 cell 時，上方/左方格子已是各自的最小路徑和」 | 轉移方程直接取 min |
| Sliding window #76 | 「window valid ⟺ formed == need」 | 何時擴、何時縮 |

## #235 的完整論證（2026-07-02 卡點）

1. Invariant：p、q 永遠在以 curr 為根的子樹裡（含 curr）
2. 下沉維持它：兩個都 < curr → 都在左子樹 → 走左（右同理）
3. split（qv ≤ curr.val ≤ pv）為何 = **最低**：此刻 p、q 分居兩側（或其一 == curr）。
   再往下**任何一步**都要選邊，選左丟 q、選右丟 p——腳下子樹必失其一。
   所以 curr 是最後一個「同時罩住兩者」的節點。∎

## 常見錯誤模式（自己的卡點史）

- **拿步驟冒充**：「我把 node push 進 stack 然後...」（#94、#239 初版）
- **拿 trigger 冒充 state**：「兩邊 size 差 2 的時候搬」是觸發條件，state 是「|diff| ≤ 1」（#295）
- **循環論證**：「為什麼 4 是 LCA？因為 LCA 就是 4」（#235）——結論不能當理由
- **措辭漏邊界**：「在左右子樹中」漏了「含 curr 自己」→ 對應 code 裡 `>=` vs `>` 的差別（#235）

## 複習時問自己

1. Binary search 的 invariant 是哪句話？它怎麼推出「lo > hi 就能 return -1」？
2. #235 站在 curr 上還沒 return 時，p、q 在哪？為什麼 split 那刻 curr 一定是「最低」？
3. 「兩邊 size 差 2 就搬一個」是 invariant 嗎？不是的話，真正的 invariant 是什麼？
4. 你的 invariant 句子裡有沒有動詞動作？有的話怎麼改寫成狀態？
