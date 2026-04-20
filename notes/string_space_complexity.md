# 字串儲存的空間複雜度（容易漏的 O(N) 因子）

> 建立日：2026-04-21，由 127 Word Ladder 把 `O(M·N²)` 寫成 `O(M·N)` 而生

## 核心觀念：「存一個東西」的空間 = 那個東西本身的大小

**字串不是 O(1) entry**。存一個長度 N 的字串，空間就是 **O(N)**。
無論這個字串被存在哪裡——**變數、list 元素、dict key、dict value、set member、函式參數**——它佔的記憶體都一樣。

> Dict key 不是魔法。它就是一個字串，該多大就多大。

## 判斷 space 的兩步驟

寫複雜度前，問自己：

1. **有多少個 entry？**（M、K、N 等數量）
2. **每個 entry 本身多大？**（常被忽略，尤其是字串、tuple、list、dict）

兩者**相乘**才是總空間。

## 對照表（容易誤判的 pattern）

| 寫法 | 容易誤判 | 實際 |
|------|----------|------|
| `d = {"*ot": [...]}` | 「key 就一個，O(1) 空間」 | key 是長度 N 字串 → **O(N)** |
| `seen = set(words)` | 「M 個元素 → O(M)」 | 每個 word O(N) → **O(M·N)** |
| `result = [word for ...]` | 「list 存 K 個 → O(K)」 | 若每個是字串 → **O(K·N)** |
| `path = list(string)` | 「O(N) 應該 OK」 | 每個 char 還是 O(1)，所以確實 O(N) |
| `parent = [i for i in range(n)]` | O(n) | 這個對，因為 int 是 O(1) |
| `memo = {(i, j): val}` | 「key O(1)」 | tuple of 2 ints 還是 O(1)；tuple of 2 strings 才是 O(N) |

## Hash 也是 O(N) 時間

```python
d["hello"] = 1     # hash("hello") 要讀過全部 5 個 char → O(N)
word in seen       # 查找字串也是 O(N) time（hash + equality check）
```

這也印證「字串本身需要 O(N)」——連**用它當 key 查表**都需要 O(N) 工作量。
所以「dict/set 存字串查 O(1)」這句話嚴格來說是 **O(N) 但當作 O(1)**（若字串長度視為常數）。當 N 很長時要明寫。

## 經典例子：127 Word Ladder

```python
wordSet = defaultdict(list)
for word in wordList:                      # M 個字
    for i in range(len(word)):             # 每字 N 個位置
        pattern = word[:i] + '*' + word[i+1:]   # slice 本身 O(N) time + 產生 O(N) 字串
        wordSet[pattern].append(word)
```

**Space 分析**：
- 產出多少 (key, value) pair？→ **M·N** 個
- 每 pair 多大？→ key O(N) + value 存一個 word 是 O(N) = **O(N)**
- 總空間：M·N × O(N) = **O(M·N²)** ✓

**Time 分析（同樣道理）**：
- `word[:i] + '*' + word[i+1:]` slice + concat **本身就是 O(N) time**（Python 字串不可變，要複製）
- 對每個 word 做 N 次 slice → O(N²) per word
- M 個 word → 總共 **O(M·N²)** time

把 `O(M·N)` 寫成答案就漏掉這個第二個 N。

## 其他常見會踩到的題目

| 題目 | 容易漏的 N |
|------|----------|
| 127 Word Ladder | wildcard pattern key + value 都是 O(N) 字串 |
| 49 Group Anagrams | sorted(word) 當 key → O(N log N) time per word，key 仍佔 O(N) space |
| 139 Word Break | memo key 若用 substring 要算 O(N) |
| 211 Add & Search Word | Trie 存字串，每個 word 插入 O(N) time + O(N) space per path |
| 295 Find Median | int 資料則無此問題（int O(1)） |

## 複習時問自己

1. 我現在把什麼存進 dict / set / list？**每個元素本身幾 byte？**
2. 如果是字串/tuple/list，**長度有 bound 嗎？** N 被壓在 constraint 裡嗎？
3. Slice（`s[i:j]`）和 concat（`a + b`）有額外 time cost 嗎？是不是 O(N)？
4. 如果把字串換成 index（整數），space 會降到多少？是否可以這樣 trade-off？
