"""
LeetCode 875. Koko Eating Bananas
Difficulty: Medium
Tags: Array
URL: https://leetcode.com/problems/koko-eating-bananas/

Problem:
    Koko loves to eat bananas. There are n piles of bananas, the i-th pile
    has piles[i] bananas. The guards have gone and will come back in h hours.

    Koko can decide her bananas-per-hour eating speed of k. Each hour, she
    chooses some pile of bananas and eats k bananas from that pile. If the
    pile has less than k bananas, she eats all of them instead and will not
    eat any more bananas during this hour.

    Koko likes to eat slowly but still wants to finish eating all the
    bananas before the guards return.

    Return the minimum integer k such that she can eat all the bananas
    within h hours.

    Example 1:
        Input: piles = [3,6,7,11], h = 8
        Output: 4
∫
    Example 2:
        Input: piles = [30,11,23,4,20], h = 5
        Output: 30

    Example 3:
        Input: piles = [30,11,23,4,20], h = 6
        Output: 23

    Constraints:
        - 1 <= piles.length <= 10^4
        - piles.length <= h <= 10^9
        - 1 <= piles[i] <= 10^9

思路：

      I will use a binary search first. left speed index= 1, right speed index = max(piles), then I can calculate mid then calculate current hours, 
      If the hours exceed h, it means I need to speed up, so I need to move the left index to mid+1, Otherwise, I just move the right index to the middle..
      - 事前 gate：code 前先講「哪個 input 最可能打爆我的解法」）
      如果 piles 的長度恰等於 h 的話，就可以直接 early return，直接回傳最大值就好
      <left 太慢、right 保證可行、答案在 [left,right]」+ 單調性
      gate code: piles = [1, 1, 1, 1]  or [100, 100, 100, 100, 100] h = 5


複雜度：
    n = piles 長度, k = max(piles)
    Time: O(n * log(k))
    Space: O(1) 
"""

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            m = l + (r-l) // 2
            count = 0
            for p in piles:
                count += (p + m - 1) // m
            if count > h:
                l = m+1
            else:
                r = m
        return l



if __name__ == "__main__":
    sol = Solution()

    # Test cases
    assert sol.minEatingSpeed([3, 6, 7, 11], 8) == 4, "Case 1"
    assert sol.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30, "Case 2"
    assert sol.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23, "Case 3"

    # Edge: single pile, plenty of time → eat slowly (ceil(pile/h))
    assert sol.minEatingSpeed([1000000000], 2) == 500000000, "Edge: single big pile"

    # 事後 gate：在這行下面加 >=1 個你自己想的 case（不能是上面的變體）
    # assert ...
    assert sol.minEatingSpeed([7], 2) == 4, "non-divisible:"
    print("All tests passed!")
