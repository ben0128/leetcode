"""
LeetCode 97. Interleaving String
Difficulty: Medium
Tags: String, DP, 2D DP
URL: https://leetcode.com/problems/interleaving-string/

思路：
    I want to use two-dimensional dynamic programming to solve this problem. I need to use memoization to lower the time complexity and store the results in each position that matches the answers.

複雜度：
    Time: O(m*n) 
    Space: O(n) n = s2長度
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if len(s3) != m+n:
            return False
        dp = [False]*(n+1)
        dp[0] = True
        # i 和 j 代表字串長度
        for j in range(1, n+1):
            res = dp[j-1] and s2[j-1] == s3[j-1]
            if not res:
                break
            dp[j] = res
        
        for i in range(1, m+1):
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            for j in range(1, n+1):
                dp[j] = (dp[j-1] and s2[j-1] == s3[i+j-1]) or (dp[j] and s1[i-1] == s3[i+j-1])
        
        return dp[n]
        


if __name__ == "__main__":
    s = Solution()

    # Test case 1: s1="aabcc", s2="dbbca", s3="aadbbcbcac" -> True
    assert s.isInterleave("aabcc", "dbbca", "aadbbcbcac") == True, "Case 1"

    # Test case 2: s1="aabcc", s2="dbbca", s3="aadbbbaccc" -> False
    assert s.isInterleave("aabcc", "dbbca", "aadbbbaccc") == False, "Case 2"

    # Test case 3: s1="", s2="", s3="" -> True
    assert s.isInterleave("", "", "") == True, "Case 3: all empty"

    # Edge case: one string empty
    assert s.isInterleave("", "abc", "abc") == True, "Edge: s1 empty"
    assert s.isInterleave("abc", "", "abc") == True, "Edge: s2 empty"

    # Edge case: length mismatch
    assert s.isInterleave("a", "b", "abc") == False, "Edge: length mismatch"

    print("All tests passed!")
