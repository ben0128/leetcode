---
name: problem-file-setup
description: Create a LeetCode solution file in solutions/ with the canonical Python template — docstring containing the full English problem statement (description, examples, constraints), plus 思路/複雜度 placeholders and a runnable test block. MUST be used whenever the student starts a new problem under /practice, /study, or /mock — file is created BEFORE the problem is presented in chat so the student can work from the file alone.
---

# Problem File Setup

Single source of truth for how solution files are created. All modes (`/practice`, `/study`, `/mock`) and CLAUDE.md reference this skill instead of inlining the template.

## Hard rules

1. **File created BEFORE presenting the problem in chat.** The student should be able to open the file and read the complete problem without scrolling back through chat.
2. **Problem statement is always English** — matches LeetCode original and Google interview language; also serves as English reading practice.
3. **`思路` and `複雜度` are left empty (or `TODO`)** for the student to fill in themselves; Chinese is OK here.
4. **Test cases are pre-filled** with 2–3 normal cases + 1 edge case using `assert`.
5. **`Tags:` field must NOT reveal the data structure / algorithm.** Use only the most generic tag (`Array`, `String`, `Math`, `Tree`, `Graph` if structural, etc.) — never `Heap`, `DP`, `Topological Sort`, `Union Find`, `Sliding Window`, `Two Pointers`, `Quickselect`, `Binary Search`, `Backtracking`, etc. The student must figure out the technique themselves; the file header can't leak it. (Per CLAUDE.md "出題時不要洩露資料結構/演算法".)

## Location and naming

- **Folder**: `solutions/` (difficulty is recorded in the docstring's `Difficulty:` field, NOT as a subfolder)
- **Filename**: `{number}_{snake_case_title}.py`
  - Examples: `0001_two_sum.py`, `0547_number_of_provinces.py`, `0127_word_ladder.py`
  - Number is zero-padded to 4 digits
  - Title is lowercase, underscore-separated, no punctuation

## Canonical template

```python
"""
LeetCode {number}. {title}
Difficulty: {Easy/Medium/Hard}
Tags: {comma-separated tags, e.g., Array, Hash Table}
URL: https://leetcode.com/problems/{slug}/

Problem:
    {Full problem statement in English — copy the description verbatim or paraphrase tightly}

    Example 1:
        Input: ...
        Output: ...
        Explanation: ...

    Example 2:
        Input: ...
        Output: ...

    Constraints:
        - ...
        - ...

思路：
    TODO（學生自己填；中文 OK）

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

## What to pre-fill vs. leave for the student

**Pre-fill (interviewer/tutor does this):**
- Header: number, title, difficulty, **vague tags only** (see Hard rule 5), URL
- `Problem:` block with description + 2 examples + constraints (English)
- `if __name__` test block with 2–3 cases + 1 edge case
- Empty `class Solution` with method signature matching LeetCode

**Leave empty (student fills):**
- `思路`
- `複雜度`
- Method body

## Why this exists

- Avoids drift between the 4 places that used to describe "how to create a solution file" (CLAUDE.md + 3 command files).
- Enforces the rule from `feedback_problem_file_first` memory: full problem in docstring before any chat discussion.
- English-only problem body exercises reading comprehension and matches real interview language.
