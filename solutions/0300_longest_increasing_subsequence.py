"""
LeetCode 300. Longest Increasing Subsequence
Difficulty: Medium
Tags: Array
URL: https://leetcode.com/problems/longest-increasing-subsequence/

Problem:
    Given an integer array nums, return the length of the longest strictly
    increasing subsequence.

    A subsequence is a sequence that can be derived from an array by deleting
    some or no elements without changing the order of the remaining elements.
    For example, [3, 6, 2, 7] is a subsequence of the array [0, 3, 1, 6, 2, 2, 7].

    Example 1:
        Input: nums = [10,9,2,5,3,7,101,18]
        Output: 4
        Explanation: The longest increasing subsequence is [2,3,7,101], so the
            length is 4.

    Example 2:
        Input: nums = [0,1,0,3,2,3]
        Output: 4

    Example 3:
        Input: nums = [7,7,7,7,7,7,7]
        Output: 1

    Constraints:
        - 1 <= nums.length <= 2500
        - -10^4 <= nums[i] <= 10^4

    Follow up:
        Can you come up with an algorithm that runs in O(n log n) time
        complexity?

思路：
    tails[k] = 目前掃過的元素中，所有長度為 k+1 的嚴格遞增子序列中，最小的結尾值。

    為何 tails 嚴格遞增（→ 可用 BS）：
      任何長度 k+1 的遞增子序列，砍掉結尾就是長度 k 的遞增子序列；
      被砍掉的結尾 > 剩下的最大元素 ≥ 長度 k 的最小結尾 = tails[k-1]。
      故「長度 k+1 的最小結尾」> tails[k-1]，tails 嚴格遞增。

    為何覆寫安全：
      (a) 長度不變：覆寫只動 tails[idx]，沒有縮短陣列，已達到的最大長度被完整保留。
      (b) 未來潛力變大：覆寫後 tails[idx] 變更小；結尾越小，未來能接上去的元素越多。
      所以覆寫只會「保住現狀 + 改善未來」，從不「縮短現狀」。
複雜度：
    Time: O(nlog(n))
    Space: O(n)
"""

from typing import List
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        tails = [nums[0]]
        for i in range(1, n):
            currNum = nums[i]
            insertIdx = bisect_left(tails, currNum)
            if len(tails) == insertIdx:
                tails.append(currNum)
            else:
                tails[insertIdx] = currNum
        return len(tails)


if __name__ == "__main__":
    s = Solution()

    # Case 1: classic
    assert s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4, "Case 1"

    # Case 2: dups + non-monotonic
    assert s.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4, "Case 2"

    # Case 3: all same
    assert s.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1, "Case 3"

    # Case 4: strictly increasing
    assert s.lengthOfLIS([1, 2, 3, 4, 5]) == 5, "Case 4: already increasing"

    # Case 5: strictly decreasing
    assert s.lengthOfLIS([5, 4, 3, 2, 1]) == 1, "Case 5: decreasing"

    # Edge: single element
    assert s.lengthOfLIS([42]) == 1, "Edge: single"

    # Edge: negative numbers
    assert s.lengthOfLIS([-1, 3, -2, 5, -3]) == 3, "Edge: negatives"

    print("All tests passed!")
