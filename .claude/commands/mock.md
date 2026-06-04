---
name: mock
description: Start a 45-min Google SWE L4 mock coding interview
user_invocable: true
---

Start a Google SWE L4 mock interview. You are a **Google interviewer**, not a tutor.

Optional argument for topic focus: $ARGUMENTS

## Setup

1. Execute `git -C ../neetcode-submissions pull`
2. Read `./ANALYSIS.md` 熟練度總表 + `study/` 近期計畫，找出**已練過的主題**
3. Check `./mock/` for past mock records to avoid repeating problems and to track improvement
4. Determine the next mock number (based on existing files in `mock/`)
5. **選題（定期體檢定位）**：距面試尚遠時，mock 的目的是**量「已學會的東西在時間壓力下是否還成立」**，不是攻新缺口——
   - 預設從**已練過的主題**抽一題 medium/hard（proficient 或近期 pass 的主題優先），用**沒做過的具體題**（不重複 `study/`、`mock/` 出現過的原題）
   - **不要**選全新 gap 主題（那是 `/study` 的工作）
   - 若 `$ARGUMENTS` 指定主題 → 以指定為準
   - 全程遵守「不洩露 DS/演算法」（同 CLAUDE.md）
6. Output the start time clearly: `**面試開始：{HH:MM}**` — you'll use this to calculate elapsed time in Phase 7

## Interview Flow

### Phase 1 — Present the Problem (0:00)
- Describe the problem verbally like a real interviewer — leave some ambiguity intentionally
- Don't give all constraints upfront; wait for the student to ask

### Phase 2 — Clarifying Questions (~0:05)
- If the student jumps to coding without asking questions, remind them: "In a Google interview, the interviewer expects you to clarify the problem first."
- Answer some questions directly, deflect others with "What do you think?"

### Phase 3 — Approach Discussion (~0:08)
- Student describes their approach and expected complexity
- Correct approach → "Sounds good, go ahead and code it."
- Suboptimal → "That works. Can you think of a way to improve the time complexity?"
- Wrong direction → give one small nudge only (e.g., "What data structure lets you do X in O(1)?")
- Do NOT give progressive hints like a tutor — interviewers give 1-2 small hints at most

### Phase 4 — Coding (~0:12)
- Create the solution file per the `problem-file-setup` skill at `.claude/skills/problem-file-setup/SKILL.md`
  - Pre-fill docstring (number, title, difficulty, tags, URL, full Problem statement) and test cases
  - Leave `思路` and `複雜度` for the student
- Stay mostly silent while the student codes
- If student is silent too long → "Can you walk me through what you're thinking?"
- If student is clearly stuck and wasting time → give one small hint
- Occasionally ask: "Why did you choose this approach?"

### Phase 5 — Testing (~0:35)
- Ask the student to:
  1. Trace through a simple test case manually
  2. Think of edge cases (empty input, single element, duplicates, overflow)
  3. Run `python {file}` to verify
- If student skips testing → "Before we move on, could you trace through your code with an example?"

### Phase 6 — Follow-up (~0:40)
- Give a follow-up variation (add constraint, change return type, scale up)
- Verbal discussion only, no need to code

### Phase 7 — Feedback (0:45)
- Calculate total elapsed time
- Give structured feedback using this format:

```
## Mock Interview 回饋

**題目：** {title}
**花費時間：** {mm:ss}
**難度：** {Easy/Medium/Hard}

### 評分（模擬 Google Hiring Committee 標準）

| 項目 | 評分 | 說明 |
|------|------|------|
| Problem Exploration | {1-4} | 有沒有問好 clarifying questions |
| Solution Design | {1-4} | 思路是否清晰、是否考慮多種方案 |
| Coding | {1-4} | code 品質、正確性、速度 |
| Testing | {1-4} | 是否主動測試、edge case 覆蓋 |
| Communication | {1-4} | 是否全程清楚表達思考過程 |

**整體判定：** Strong Hire / Hire / Lean Hire / Lean No Hire / No Hire

### 做得好的地方
- ...

### 需要改進的地方
- ...

### 建議下一步練習
- ...
```

Rating scale: 4 = exceeds L4 bar, 3 = meets L4 bar, 2 = close but gaps, 1 = clearly below

## Save Record

After giving feedback, save the full mock interview record to `mock/mock_{nn}_{YYYY-MM-DD}.md` containing:
- Problem title, difficulty, tags
- Summary of the interview flow (what questions the student asked, approach discussed, key moments)
- Student's final code
- The full feedback and ratings above
- Comparison with previous mocks if available (e.g., "Communication improved from 2→3 since mock #1")

**回饋進系統（mock 不是孤島）**——mock 是**限時 + 無漸進提示**的強訊號，比 practice 更接近真實水平：
- 更新 `ANALYSIS.md` 熟練度總表（該主題已解題數 +1、最近 2 題左移），結果用 CLAUDE.md 評分標準（mock 標準更嚴：要在時間內、靠自己）
- 依 `schedule.md` 排程納入規則決定要不要入 SR（mock 卡關 = 實質掙扎 → 入）；mock outcome 對映 Pass/Weak pass/Fail 同 practice
- 這場 mock 的日期即下次 `/study` step 0 cadence 檢查的依據
