"""
LeetCode 394. Decode String
Difficulty: Medium
Tags: Stack, String, Recursion
URL: https://leetcode.com/problems/decode-string/

Problem:
    Given an encoded string, return its decoded string.

    The encoding rule is: k[encoded_string], where the encoded_string inside
    the square brackets is being repeated exactly k times. Note that k is
    guaranteed to be a positive integer.

    You may assume that the input string is always valid; there are no extra
    white spaces, square brackets are well-formed, etc. Furthermore, you may
    assume that the original data does not contain any digits and that digits
    are only for those repeat numbers, k. For example, there will not be input
    like 3a or 2[4].

    The test cases are generated so that the length of the output will never
    exceed 10^5.

    Example 1:
        Input: s = "3[a]2[bc]"
        Output: "aaabcbc"

    Example 2:
        Input: s = "3[a2[c]]"
        Output: "accaccacc"

    Example 3:
        Input: s = "2[abc]3[cd]ef"
        Output: "abcabccdcdcdef"

    Constraints:
        - 1 <= s.length <= 30
        - s consists of lowercase English letters, digits, and square brackets '[]'.
        - s is guaranteed to be a valid input.
        - All the integers in s are in the range [1, 300].

思路：
    iterative + stack 會比較直覺, 先stack = [] 蒐集每一層的字串, 當進入下一層時(遇到'[')把上一層的結果 存入stack中, 等到遇到']' 在pop出接起來
    recursive 會跑一個for 迴圈, return (word, idx)：caller 拿到 idx 才知道內層讀到哪、要從哪繼續
複雜度：
    n = 所有 數字*字串 後接在一起的最終長度
    Time: O(n)
    Space: O(n) 
"""


class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        def recursive(idx):
            num = 0
            word = []
            # for k, c in enumerate(s[idx:], idx):
            while idx < n:
                c = s[idx]
                if c.isdigit():
                    num = num*10 + int(c)
                elif c == '[':
                    tmpWords, nxtIdx = recursive(idx+1)
                    word.append(''.join(tmpWords)*num)
                    idx, num = nxtIdx, 0
                elif c == ']':
                    return [word, idx]
                else:
                    word.append(c)
                idx += 1
            return [word, None]
        return ''.join(recursive(0)[0])




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
