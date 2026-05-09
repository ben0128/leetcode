"""
LeetCode 560. Subarray Sum Equals K
Difficulty: Medium
Tags: Array
URL: https://leetcode.com/problems/subarray-sum-equals-k/

Problem:
    Given an array of integers nums and an integer k, return the total number
    of subarrays whose sum equals to k.

    A subarray is a contiguous non-empty sequence of elements within an array.

    Example 1:
        Input: nums = [1,1,1], k = 2
        Output: 2
        Explanation: The two subarrays are nums[0..1] and nums[1..2], both
        with sum = 2.

    Example 2:
        Input: nums = [1,2,3], k = 3
        Output: 2
        Explanation: The two subarrays are [1,2] and [3].

    Constraints:
        - 1 <= nums.length <= 2 * 10^4
        - -1000 <= nums[i] <= 1000
        - -10^7 <= k <= 10^7

思路：
    for loop 算出 preflix sum, 再透過 visited 查找已經出現過的preflix, count += visited[preflix- k] 就能累加答案

複雜度：
    n = len(nums)
    Time: O(n)
    Space: O(n)
"""

from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        visited = defaultdict(int)
        visited[0] = 1
        n = len(nums)
        preflix = 0
        count = 0
        
        for i in range(n):
            preflix += nums[i]
            count += visited[preflix - k]
            visited[preflix] += 1
        return count


if __name__ == "__main__":
    s = Solution()
    # Test cases
    assert s.subarraySum([1, 1, 1], 2) == 2, "Case 1"
    assert s.subarraySum([1, 2, 3], 3) == 2, "Case 2"
    assert s.subarraySum([3, 4, 7, 2, -3, 1, 4, 2], 7) == 4, "Case 3: with negatives"
    # Edge cases
    assert s.subarraySum([1], 1) == 1, "Edge: single element match"
    assert s.subarraySum([1], 0) == 0, "Edge: single element no match"
    assert s.subarraySum([0, 0, 0], 0) == 6, "Edge: zeros (tricky)"
    assert s.subarraySum([1, -1, 0], 0) == 3, "Edge: signed cancel"
    print("All tests passed!")
