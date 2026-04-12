---
name: study
description: Generate a 5-problem study plan based on weakness analysis
user_invocable: true
---

Generate a focused 5-problem study plan for Google SWE L4 prep.

Optional argument for topic focus: $ARGUMENTS

## Steps

1. **讀取歷史紀錄**
   - Read `./ANALYSIS.md` to review current weaknesses
   - Read all existing files in `./study/` to determine the next plan number and avoid repeating already-completed problems
   - Execute `git -C ../neetcode-submissions pull` to get latest submissions

2. **快速複習（如果有之前的 notes）**
   - 掃描 `./notes/` 裡的筆記，挑 1-2 個跟本次計畫主題相關的「複習時問自己」問題抽問學生
   - 確認上次學的概念還記得，再開始新的計畫

3. **設計 5 題計畫**，遵守以下規則：

### Plan Design Rules
- **題目組成**：2 題弱項主題 + 2 題中等熟練主題 + 1 題新主題或 hard 挑戰
- **難度分布**：至少 3 題 medium、至少 1 題 hard
- **不重複**：不出 `study/` 資料夾中已完成（✅ 或 ⚠️）的題目，除非標記為需要重練
- **漸進式**：如果上一份計畫某主題表現差，這次加強同主題但換題目
- If user specifies a topic, weight 3 of 5 problems toward that topic

4. **輸出計畫**，格式如下：

```
## 讀書計畫 #{number} — {YYYY-MM-DD}
主題重點：{focus areas}

| # | 題目 | 難度 | 主題 | 為什麼選這題 |
|---|------|------|------|-------------|
| 1 | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... |
| 4 | ... | ... | ... | ... |
| 5 | ... | ... | ... | ... |

建議順序：先做 #{n}（暖身）→ #{n} → #{n} → #{n} → #{n}（挑戰）
預估總時間：{X} 小時
```

5. **存檔到 `study/plan_{nn}_{YYYY-MM-DD}.md`**
   - 包含計畫內容和進度追蹤表格（初始狀態全部為 `—`）
   - 編號接續 `study/` 資料夾中最大的編號

6. **問學生要從哪題開始**，然後以 `/practice` 助教模式引導該題：
   - Create the solution file using the template and naming convention from `/practice`
   - File location: `easy/`, `medium/`, or `hard/` based on difficulty
   - Filename: `{number}_{snake_case_title}.py`
   - Follow the full practice flow (approach discussion → coding → optimize → teach back → follow-up → timing)
   - After solving, commit the solution file

7. **每完成一題，立即更新** `study/plan_{nn}_{YYYY-MM-DD}.md` 的進度欄位：
   - 結果：✅ = 獨立解出最優解 / ⚠️ = 需要提示或非最優 / ❌ = 無法解出
   - 花費時間（實際分鐘數）
   - 筆記（掙扎點或收穫）

8. **全部 5 題完成後**，append 摘要到 `./ANALYSIS.md` 的「讀書計畫紀錄」section：

```
### Plan #{number} — {YYYY-MM-DD}
主題重點：{focus areas}

| # | 題目 | 結果 | 花費時間 | 筆記 |
|---|------|------|----------|------|
| 1 | ... | ✅/⚠️/❌ | ... | ... |
| 2 | ... | ... | ... | ... |

**整體觀察：** {patterns noticed, improvements, recurring issues}
**下次建議加強：** {topics to focus next}
```
