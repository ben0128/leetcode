# Nested Parsing with Stack（嵌套結構的 stack 模式）

> 心智模型建立日：2026-04-18，由 394 Decode String 重度卡關而生

## 核心類比：手動管 call stack

recursion 時 Python 自動管 call stack：
- outer 函式執行中呼叫 inner → outer 的 local vars 被凍結（壓入 call stack）
- inner 跑完 return → Python 從 call stack 恢復 outer，outer 拿到 inner 的回傳值繼續

**iterative stack 做的事情一模一樣，只是你手動管：**
- 遇到「進入內層」標記（如 `[`）→ push outer local vars 到 stack，重置環境進入內層
- 遇到「離開內層」標記（如 `]`）→ pop outer，把 inner 結果接回 outer

## 心智模型：抽屜 + 桌面

```
      ┌────────────────────┐
stack  │ (3, "")            │  最外層的現場（抽屜最底）
      │ (2, "a")           │  第二層的現場
      │                    │
char  │ "c"                │  當前正在寫的（桌面）
      └────────────────────┘
```

- `[` = **把桌面上的東西掃進抽屜**，桌面重新乾淨
- `]` = **拉開最上面的抽屜**，把裡面的東西 + 桌面的成果組合成新的桌面內容

## 最關鍵：每次只想「一層」

卡住的典型原因：**試圖同時想 3 層嵌套發生什麼事**。大腦記不住。

正確思考方式：
1. **假裝沒有嵌套**，只處理一層（例如先想 `3[a]`，不要想 `3[a2[c]]`）
2. 寫出「一層的 3 個動作」：
   - **進入時**：從上層拿什麼？（從 stack pop 出來的東西）
   - **處理中**：這一層怎麼累積狀態？
   - **離開時**：要傳給上層什麼？（組合成新狀態，更新當前變數）
3. **Stack 是大腦的延伸**：你只關心當前一層，其他層由 stack 記得

## 模板

```python
def parse_nested(s: str):
    stack = []
    # 當前層的 local state（例如累積器、計數器）
    cur_state = initial_state()

    for c in s:
        if c is "進入 inner 標記":          # 例如 '['
            stack.append(cur_state)         # 把當前層現場存起來
            cur_state = fresh_state()       # 重置進入內層

        elif c is "離開 inner 標記":        # 例如 ']'
            inner_result = cur_state        # 內層解完的結果
            cur_state = stack.pop()         # 拿回外層現場
            cur_state = merge(cur_state, inner_result)  # 把內層接回外層

        else:
            cur_state = update(cur_state, c)  # 處理當前層內的普通字元

    return finalize(cur_state)
```

## 常見 bug（394 踩過的）

1. **進入 `[` 時硬寫空字串**，不是 `push (num, char)` → 外層的累積結果丟失，nested 完全壞掉
2. **離開 `]` 時 pop 出來的外層 state 不用** → 等於沒接回外層
3. **把 stack 當答案累積器**，最後 `''.join(stack)` → 違反 stack 用途，應該用一個獨立變數 accumulator

## 適用題目（一通百通）

| 題目 | 一層的「state」| stack 存什麼 | 進入標記 | 離開標記 |
|------|------------|-------------|---------|---------|
| 394 Decode String | `(num, char)` | 外層 (num, char) | `[` | `]` |
| 726 Number of Atoms | Counter dict | 外層 dict | `(` | `)` |
| 227 Basic Calculator II | `(sign, result, num)` | — | — | 運算子 |
| 224 Basic Calculator | `(sign, result)` | 外層 (sign, result) | `(` | `)` |
| 636 Exclusive Time | 進入時間 + 累積時間 | 進入時間 | `start` | `end` |
| 1096 Brace Expansion II | 當前集合 | 外層集合 | `{` | `}` |

**這些題的差別只在 state 的「型態」不同**（字串 / dict / 數字 / 集合），stack 的 push/pop 時機和接回邏輯是同一個 pattern。

## 複習時問自己

1. 進入內層時要 push 什麼？為什麼？（答：外層的**所有** local state，否則離開時拿不回來）
2. 離開內層時，怎麼把內層結果接回外層？
3. Stack 裡的資料型態是什麼？為什麼不是兩個獨立 stack？
4. 為什麼這個 pattern 也可以用 recursion 寫？兩種版本哪個面試官比較接受？（答：iterative 更乾淨，面試官通常偏好；但會要你能口述 recursion 版本）
