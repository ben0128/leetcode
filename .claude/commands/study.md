---
name: study
description: Generate a 5-problem study plan based on weakness analysis
user_invocable: true
---

Generate a focused 5-problem study plan for Google SWE L4 prep.

Optional argument for topic focus: $ARGUMENTS

## Steps

1. Read `./ANALYSIS.md` to review current weaknesses and past study plan results
2. Execute `git -C ../neetcode-submissions pull` to get latest submissions
3. Check which problems in `../neetcode-submissions/` have been solved recently
4. Design a 5-problem plan following these rules:

### Plan Design Rules
- **題目組成**：2 題弱項主題 + 2 題中等熟練主題 + 1 題新主題或 hard 挑戰
- **難度分布**：至少 3 題 medium、至少 1 題 hard
- **不重複**：不出 ANALYSIS.md 中「讀書計畫紀錄」裡已經完成過的題目（除非標記為需要重練）
- **漸進式**：如果上一份計畫某主題表現差，這次加強同主題但換題目
- If user specifies a topic, weight 3 of 5 problems toward that topic

### Output Format

```
## 讀書計畫 #{number} — {date}
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

5. Ask the student which problem they want to start with, then switch to practice mode for that problem.
6. After all 5 problems are completed, append a study plan summary to `./ANALYSIS.md` under the "讀書計畫紀錄" section, using this format:

```
### Plan #{number} — {date}
主題重點：{focus areas}

| # | 題目 | 結果 | 花費時間 | 筆記 |
|---|------|------|----------|------|
| 1 | ... | ✅/⚠️/❌ | ... | 掙扎點或收穫 |
| 2 | ... | ... | ... | ... |

**整體觀察：** {patterns noticed, improvements, recurring issues}
**下次建議加強：** {topics to focus next}
```

Results key: ✅ = solved optimally without help, ⚠️ = solved with hints or suboptimal, ❌ = could not solve
