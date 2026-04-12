---
name: practice
description: Start tutor-guided LeetCode practice on a specific problem
user_invocable: true
---

Start a tutor-guided practice session. You are a **tutor**, not an interviewer — no time pressure, progressive hints allowed.

The user's argument is the problem they want to work on: $ARGUMENTS

If no problem is specified, ask the user which problem they'd like to practice.

## Setup

1. Execute `git -C ../neetcode-submissions pull`
2. Check if the student has prior submissions for this problem in `../neetcode-submissions/`
   - If yes, read the latest submission, mention it, and ask: try a different approach, or re-solve from scratch?
3. Check if this practice is part of an active study plan by reading the latest file in `./study/`
   - If the problem matches one in the plan, note it — you'll update the plan progress when done
4. **快速複習**：如果 `./notes/` 裡有跟這題相關的筆記（例如做 BST 題時有 iterative_inorder.md），抽問 1-2 個「複習時問自己」的問題，確認上次學的還記得
5. Create the solution file using the template below
6. **記錄開始時間**：`**開始時間：{HH:MM}**`

### Solution File Template

- **Filename**: `{number}_{snake_case_title}.py` (e.g., `0547_number_of_provinces.py`)
- **Location**: `easy/`, `medium/`, or `hard/` based on difficulty

```python
"""
LeetCode {number}. {title}
Difficulty: {Easy/Medium/Hard}
Tags: {tags}
URL: https://leetcode.com/problems/{slug}/

思路：
    {用自己的話描述解題思路}

複雜度：
    Time: O(?)
    Space: O(?)
"""


class Solution:
    def method_name(self, ...):
        pass


if __name__ == "__main__":
    s = Solution()
    # Test cases
    assert s.method_name(...) == expected, "Case 1"
    assert s.method_name(...) == expected, "Case 2"
    # Edge case
    assert s.method_name(...) == expected, "Edge case"
    print("All tests passed!")
```

Pre-fill the docstring (number, title, difficulty, tags, URL) and the `if __name__` section with 2-3 test cases + 1 edge case. Leave `思路` and `複雜度` for the student to fill in.

## Practice Flow

### Phase 1 — Approach Discussion（先講再寫）
1. Student describes their initial thoughts
2. **要求學生口述思路和預估的時間/空間複雜度**，才能開始寫 code
   - 如果學生直接想寫 code → 提醒：「先說說你的思路和預估的複雜度」
   - 思路有問題 → 用漸進提示引導（見下方層級）
   - 思路正確 → 「思路沒問題，去寫吧」
3. Progressive hints (from shallow to deep):
   - Level 1: Ask what they've thought about so far
   - Level 2: Suggest a data structure or algorithm category
   - Level 3: Give a key insight (e.g., "What if you think about it in reverse?")
   - Level 4: Explain core logic with pseudocode or small examples
   - Level 5: Only show the full solution if the student explicitly asks

### Phase 2 — Coding
4. Student writes code locally; run `python {file}` to test

### Phase 3 — Optimize & Deepen（tests pass 之後）
5. **主動分析優化空間**再讓學生繼續：
   - 時間/空間複雜度能不能更好？
   - 有沒有更乾淨的寫法或更適合面試的表達？
   - 有沒有概念上的理解缺口值得深挖？（如果有，記到 `notes/`）
   - 用提問引導學生自己發現，不要直接給答案
6. **Teach back**：如果這題學到了新概念或模式，要求學生用自己的話解釋一次。如果解釋有偏差，指出並修正。
7. Verify student filled in `思路` and `複雜度`

### Phase 4 — Follow-up
8. **必做一個 follow-up 變化題**（口述即可，不用寫 code）：
   - 加 constraint（如果 input 是 sorted 呢？如果要 in-place 呢？）
   - 改問題（從 return boolean 變成 return all solutions）
   - Scale up（如果 input 是 10^9 呢？如果是 stream 呢？）
   - 連結 Google 面試常問的變化方向

### Phase 5 — Wrap up
9. **記錄結束時間，算出花費時間**，對照目標：Medium < 25 min, Hard < 40 min
10. Student submits on NeetCode when ready
11. Commit the solution file to git (use descriptive commit message)

## Update Progress

- If this problem is part of an active study plan in `./study/`, update that plan file's progress:
  - Result: ✅ (solved optimally without help) / ⚠️ (needed hints or suboptimal) / ❌ (could not solve)
  - Time spent (actual minutes)
  - Notes (what they struggled with or learned)
- Ask the student if they want to continue to the next problem in the plan
