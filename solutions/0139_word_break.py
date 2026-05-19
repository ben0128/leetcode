"""
LeetCode 139. Word Break
Difficulty: Medium
Tags: String
URL: https://leetcode.com/problems/word-break/

Problem:
    Given a string s and a dictionary of strings wordDict, return true if s can
    be segmented into a space-separated sequence of one or more dictionary words.

    Note that the same word in the dictionary may be reused multiple times in
    the segmentation.

    Example 1:
        Input:  s = "leetcode", wordDict = ["leet","code"]
        Output: true
        Explanation: Return true because "leetcode" can be segmented as "leet code".

    Example 2:
        Input:  s = "applepenapple", wordDict = ["apple","pen"]
        Output: true
        Explanation: Return true because "applepenapple" can be segmented as
        "apple pen apple". Note that you are allowed to reuse a dictionary word.

    Example 3:
        Input:  s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
        Output: false

    Constraints:
        - 1 <= s.length <= 300
        - 1 <= wordDict.length <= 1000
        - 1 <= wordDict[i].length <= 20
        - s and wordDict[i] consist of only lowercase English letters.
        - All the strings of wordDict are unique.

思路：
    透過set 加速查找wordDict, 並從左到右 去 for loop 字串 把i當作頭, 把j當尾巴 逐一跟set比對 有找到就代表此位置可以被切割

複雜度：
    Time: O(n*n*n) 雙迴圈並切割字串
    Space: O(n) n = 字串長
"""


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(n):
            if not dp[i]:
                continue
            for j in range(i+1, n+1):
                if s[i:j] in wordSet:
                    dp[j] = True
        return dp[-1]

if __name__ == "__main__":
    sol = Solution()
    # Test cases
    assert sol.wordBreak("leetcode", ["leet", "code"]) is True, "Case 1: simple split"
    assert sol.wordBreak("applepenapple", ["apple", "pen"]) is True, "Case 2: reuse word"
    assert sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False, "Case 3: no valid split"
    # Edge cases
    assert sol.wordBreak("a", ["a"]) is True, "Edge: single char match"
    assert sol.wordBreak("ab", ["a"]) is False, "Edge: leftover char"
    # Tricky: greedy fails (must explore all splits)
    assert sol.wordBreak("aaaaaaa", ["aaaa", "aaa"]) is True, "Tricky: greedy-trap (3+4 or 4+3)"
    print("All tests passed!")
