# LeetCode Practice — Google SWE L4 Prep

一份為了準備 **Google SWE L4 面試** 而設計的 LeetCode 練習工作流，搭配 [Claude Code](https://claude.com/claude-code) 作為助教 / 面試官 / 排程引擎。

題目以 medium / hard 為主，重點在**限時思考、清楚口述思路、複習鞏固**，而不是單純堆刷題數。

---

## 三種使用模式

| 指令 | 角色 | 用途 |
|------|------|------|
| `/study` 或 `/study {topic}` | 助教 | 依弱項分析生成 5 題讀書計畫（含 1 題 SR 複習） |
| `/practice {problem}` | 助教 | 不限時引導練習，分層提示，逐步逼出解法 |
| `/mock` 或 `/mock {topic}` | Google 面試官 | 45 分鐘模擬面試，含 clarifying / coding / testing / follow-up / 回饋 |

執行時 Claude 會：

1. 用 `problem-file-setup` skill 在 `solutions/` 建好題目檔（含完整英文題幹、constraints、空白思路區）
2. 依模式不同進行引導或面試
3. 完成後更新讀書計畫紀錄、SR 排程、弱項分析

---

## 目錄結構

```
solutions/          # 解題檔案，{number}_{snake_case_title}.py
notes/              # 跨題目的概念筆記（binary search 模板、union find、iterative inorder…）
study/              # 讀書計畫紀錄 plan_{nn}_{YYYY-MM-DD}.md
mock/               # 模擬面試逐字稿與評分 mock_{nn}_{YYYY-MM-DD}.md
review/schedule.md  # 間隔重複（SR）排程：2d → 7d → 16d → 32d → mastered
ANALYSIS.md         # 弱項分析報告（題目掙扎、code quality、主題掌握度）
GOOGLE_QUESTIONS.md # Google 高頻考古題單，標記頻率（🔥🔥🔥 / 🔥🔥 / 🔥）
CLAUDE.md           # 給 Claude Code 的工作指引（模式流程、評分標準、教學態度）
```

---

## 解題檔案命名

`{number}_{snake_case_title}.py` — e.g. `0162_find_peak_element.py`

每個檔案結構：

- Docstring：完整英文題目描述（題幹 + examples + constraints）+ 思路 + 複雜度
- `class Solution`：解法本體
- `if __name__ == "__main__":`：可直接 `python solutions/xxx.py` 跑的測試

---

## 間隔重複（Spaced Repetition）

每題寫完後會被排入 `review/schedule.md`，依 **2d / 7d / 16d / 32d** 四階段複習，全部通過視為 mastered。`/study` 生成計畫時會自動把當天到期的題目塞進 5 題裡的 1 題複習槽。

---

## 環境

- Python 3（standard library only，無外部依賴）
- macOS / Linux / WSL 皆可
- 搭配 [Claude Code](https://claude.com/claude-code) 使用 slash commands；不安裝也能單純把它當解題倉庫用
