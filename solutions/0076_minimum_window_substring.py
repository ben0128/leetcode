"""
LeetCode 76. Minimum Window Substring
Difficulty: Hard
Tags: String
URL: https://leetcode.com/problems/minimum-window-substring/

Problem:
    Given two strings s and t of lengths m and n respectively, return the
    minimum window substring of s such that every character in t (including
    duplicates) is included in the window. If there is no such substring,
    return the empty string "".

    The testcases will be generated such that the answer is unique.

    Example 1:
        Input: s = "ADOBECODEBANC", t = "ABC"
        Output: "BANC"
        Explanation: The minimum window substring "BANC" includes 'A', 'B',
        and 'C' from string t.

    Example 2:
        Input: s = "a", t = "a"
        Output: "a"
        Explanation: The entire string s is the minimum window.

    Example 3:
        Input: s = "a", t = "aa"
        Output: ""
        Explanation: Both 'a's from t must be included in the window. Since
        the largest window of s only has one 'a', return empty string.

    Constraints:
        - m == s.length
        - n == t.length
        - 1 <= m, n <= 10^5
        - s and t consist of uppercase and lowercase English letters.

思路：
    透過sliding window 和 hashMap 去即時更新window內的種類和數量, 透過for loop 移動r, 當invalid時就移動完r就下一圈, 當valid時就要開始透過移動l, 更新最小值, 直到invalid
    並在每次shrink時 計算最小值 , ans 用 [l, r] 表示而不用s[l:r] 可以避免每次更新時 需要切割
    使用valid 計算有多少種類已經valid, 避免之後再比對時需要耗費大量時間
    使用sliding window 是因為 r+1時保證valid單調性, l+1時保證invalid
    

複雜度：
    Time: O(2n) => O(n) 2n = 左右兩指針都有可能loop s 一遍
    Space: O(len(types)) types = char 的種類 存在hashMap
"""
from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        if n < len(t):
            return ''
        curr = defaultdict(int)
        need = {}
        valid = 0

        for c in t:
            need[c] = need.get(c, 0) + 1
        
        needLen = len(need)
        l = 0
        ans = [0, n]
        
        for r, c in enumerate(s):
            curr[c] += 1
            if c in need and curr[c] == need[c]:
                valid += 1
            
            while valid == needLen:
                if ans[1]-ans[0] > r-l:
                    ans = [l, r]
                waitRemove = s[l]
                curr[waitRemove] -= 1
                if waitRemove in need and curr[waitRemove] < need[waitRemove]:
                    valid -= 1
                l += 1

        return s[ans[0]:ans[1]+1] if ans[1] != n else ''
            
        # need = {A:1, B:1, C:1}
        #  s = "ADOBECODEBANC",
        #       l    r         => move left now => ans = [0, 5]
        #        l   r         => continue move right 
        #        l        r    => continue move left 
        #             l   r    => keep update l until invalid
        #             l     r  => move left now and find answer 'BANC'
        #             




if __name__ == "__main__":
    sol = Solution()
    # Test cases
    assert sol.minWindow("ADOBECODEBANC", "ABC") == "BANC", "Case 1"
    assert sol.minWindow("a", "a") == "a", "Case 2: trivial match"
    assert sol.minWindow("a", "aa") == "", "Case 3: impossible"
    # Edge cases
    assert sol.minWindow("aa", "aa") == "aa", "Edge: duplicates required"
    assert sol.minWindow("ab", "b") == "b", "Edge: target at end"
    assert sol.minWindow("cabwefgewcwaefgcf", "cae") == "cwae", "Edge: tricky shrink"
    print("All tests passed!")
