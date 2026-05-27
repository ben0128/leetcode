"""
LeetCode 97. Interleaving String
Difficulty: Medium
Tags: String
URL: https://leetcode.com/problems/interleaving-string/

Problem:
    Given strings s1, s2, and s3, find whether s3 is formed by an
    interleaving of s1 and s2.

    An interleaving of two strings s and t is a configuration where s and t
    are divided into n and m substrings respectively, such that:
        - s = s_1 + s_2 + ... + s_n
        - t = t_1 + t_2 + ... + t_m
        - |n - m| <= 1
        - The interleaving is s_1 + t_1 + s_2 + t_2 + ... or
          t_1 + s_1 + t_2 + s_2 + ...

    Note: a + b is the concatenation of strings a and b.

    Example 1:
        Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
        Output: true
        Explanation: One way to obtain s3 is:
        Split s1 into s1 = "aa" + "bc" + "c", and
        s2 into s2 = "dbbc" + "a".
        Interleaving the two splits, we get
        "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".

    Example 2:
        Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
        Output: false
        Explanation: Notice how it is impossible to interleave s2 with any
        other string to obtain s3.

    Example 3:
        Input: s1 = "", s2 = "", s3 = ""
        Output: true

    Constraints:
        - 0 <= s1.length, s2.length <= 100
        - 0 <= s3.length <= 200
        - s1, s2, and s3 consist of lowercase English letters.


思路：
    1. 演算法骨架：
       (a) 預檢 len(s3) != m+n → 直接 return False
       (b) 確保 m >= n（若 n>m 交換 s1/s2），讓 rolling array 跑短的
       (c) Init dp[0..n]=False，dp[0]=True；第 0 row 只用 s2：
           dp[j] = dp[j-1] and s2[j-1]==s3[j-1]（一旦 False 後面全 False → break）
       (d) i=1..m row：先更新 dp[0]（只能來自 s1 上方）；
           inner loop 用轉移方程 dp[j+1] = (dp[j+1] and s1[i]==s3[i+j+1])
                                       or (dp[j]   and s2[j]==s3[i+j+1])
       (e) 答案 dp[n]
    2. 資料結構 + 理由：1D rolling array dp[0..n]。
       每 row 只依賴上一 row 的同位 dp[j+1] 與當前 row 已更新的 dp[j]，
       不需保留整 2D table → 空間從 O(m·n) 壓到 O(min(m,n))
    3. Invariant（inner loop 第 i row、處理到 j 時）：
       (a) 讀 dp[j+1] 時 = 上一 row 的值 (= dp[i-1][j+1])
           讀 dp[j]   時 = 當前 row 已更新的值 (= dp[i][j])
       (b) 寫完 dp[j+1] 後 = 當前 row 的值 (= dp[i][j+1])
       這就是「右半（上一 row）OR 左半（當前 row）」能正確運作的原因
    4. 複雜度：Time O(m·n)；Space O(min(m,n)+1) = O(min(m,n))

複雜度：
    Time: O(m·n) m=len(s1), n=len(s2)
    Space: O(min(m,n))
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, p = len(s1), len(s2), len(s3)
        if m+n != p:
            return False
        # 讓 s1 長度大於 s2
        if n > m:
            s1, s2 = s2, s1
            m, n = n, m
        
        dp = [False]*(n+1)
        dp[0] = True

        for j in range(1, n+1):
            if dp[j-1] and s2[j-1] == s3[j-1]:
                dp[j] = True
            else:
                break
        
        for i in range(m):
            if not (dp[0] and s3[i] == s1[i]):
                dp[0] = False
            
            for j in range(n):
                dp[j+1] = (dp[j+1] and s1[i] == s3[i+j+1]) or (dp[j] and s2[j] == s3[i+j+1])
        return dp[-1]



if __name__ == "__main__":
    s = Solution()
    # Test cases
    assert s.isInterleave("aabcc", "dbbca", "aadbbcbcac") == True, "Case 1"
    assert s.isInterleave("aabcc", "dbbca", "aadbbbaccc") == False, "Case 2"
    assert s.isInterleave("", "", "") == True, "Case 3: all empty"
    # Edge cases
    assert s.isInterleave("", "abc", "abc") == True, "Edge: s1 empty"
    assert s.isInterleave("abc", "", "abc") == True, "Edge: s2 empty"
    assert s.isInterleave("a", "b", "abc") == False, "Edge: length mismatch"
    print("All tests passed!")
