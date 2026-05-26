"""
LeetCode 3. Longest Substring Without Repeating Characters
Difficulty: Medium
Tags: String, Hash Table
URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Problem:
    Given a string s, find the length of the longest substring without
    duplicate characters.

    Example 1:
        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.

    Example 2:
        Input: s = "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.

    Example 3:
        Input: s = "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
        Notice that the answer must be a substring, "pwke" is a
        subsequence and not a substring.

    Constraints:
        - 0 <= s.length <= 5 * 10^4
        - s consists of English letters, digits, symbols and spaces.

思路：
    1. 骨架：right 從 0 跑到 n-1；查 hashmap；不在 / 在但 stale → 直接擴；在且 in-window → 跳 left。每輪更新 hashmap[c] = right 並比 max length。
    2. 資料結構：hashmap 把 dup lookup O(window) → O(1)。
    3. Invariant（迴圈尾）：(1) 窗口無 dup；(2) hashmap[c] = c 最近 index。
    4. 複雜度：Time O(n)，Space O(min(n, |charset|))。

複雜度：
    Time: O(n) n = len(s)
    Space: O(m) m = numbers of types in s
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charDict = {}  
        l = 0
        maxLen = 0
        for r in range(len(s)):
            c = s[r]
            # 重複的字串在窗內 且 
            if c in charDict and charDict[c] >= l:
                l = charDict[c] + 1
            else:
                maxLen = max(maxLen, r-l+1)
            charDict[c] = r
        return maxLen
            




if __name__ == "__main__":
    sol = Solution()
    # Test cases
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3, "Case 1"
    assert sol.lengthOfLongestSubstring("bbbbb") == 1, "Case 2"
    assert sol.lengthOfLongestSubstring("pwwkew") == 3, "Case 3"
    # Edge cases
    assert sol.lengthOfLongestSubstring("") == 0, "Empty string"
    assert sol.lengthOfLongestSubstring(" ") == 1, "Single space"
    assert sol.lengthOfLongestSubstring("dvdf") == 3, "Tricky: dvdf -> vdf"
    print("All tests passed!")
