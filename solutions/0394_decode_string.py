"""
LeetCode 394. Decode String
Difficulty: Medium
Tags: Stack, String, Recursion
URL: https://leetcode.com/problems/decode-string/

思路：
    Iterative stack。關鍵 insight：`char` 是答案累積器，stack 只存「進入 [ 之前的外層快照 (num, char)」。
    - digit：累積多位數 `num = num*10 + int(c)`
    - `[`：push (num, char) 暫存外層；重置 num=0, char=''
    - `]`：pop 外層 (prev_num, prev_str)，`char = prev_str + char * prev_num`
    - 字母：append 到 char
    結尾 return char。

    常見 bug：
    1. `[` 時 push [num, '']（硬寫空字串）→ 外層 char 丟失，nested 崩潰
    2. `]` 時不用 popC，只推回 [1, char*popN] → 把 stack 當成答案累積器，違反用途

複雜度：
    Time: O(N) — N = 解碼後輸出長度（可能遠大於 input）
    Space: O(N) — char 累積器 + stack 中各層外層字串加總
"""


class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        char = ''
        stack = []
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                stack.append([num, char])
                num, char = 0, ''
            elif c == ']':
                popN, popC = stack.pop()
                char = popC + popN * char
            else:
                char += c
        return char




if __name__ == "__main__":
    sol = Solution()
    # Example 1
    assert sol.decodeString("3[a]2[bc]") == "aaabcbc", "Case 1"
    # Example 2: nested
    assert sol.decodeString("3[a2[c]]") == "accaccacc", "Case 2 (nested)"
    # Example 3: multi-segment
    assert sol.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef", "Case 3 (multi)"
    # Edge: no brackets
    assert sol.decodeString("abc") == "abc", "Edge: no brackets"
    # Edge: double-digit multiplier
    assert sol.decodeString("10[a]") == "aaaaaaaaaa", "Edge: double digit"
    # Edge: deeply nested
    assert sol.decodeString("2[2[b]3[a]]") == "bbaaabbaaa", "Edge: deep nesting"
    print("All tests passed!")
