"""
LeetCode 162. Find Peak Element
Difficulty: Medium
Tags: Array, Binary Search
URL: https://leetcode.com/problems/find-peak-element/

Problem:
    A peak element is an element that is strictly greater than its neighbors.

    Given a 0-indexed integer array `nums`, find a peak element, and return its
    index. If the array contains multiple peaks, return the index to any of the
    peaks.

    You may imagine that `nums[-1] = nums[n] = -infinity`. In other words, an
    element is always considered to be strictly greater than a neighbor that is
    outside the array.

    You must write an algorithm that runs in O(log n) time.

    Example 1:
        Input: nums = [1,2,3,1]
        Output: 2
        Explanation: 3 is a peak element and your function should return the
        index number 2.

    Example 2:
        Input: nums = [1,2,1,3,5,6,4]
        Output: 5
        Explanation: Your function can return either index number 1 where the
        peak element is 2, or index number 5 where the peak element is 6.

    Constraints:
        - 1 <= nums.length <= 1000
        - -2^31 <= nums[i] <= 2^31 - 1
        - nums[i] != nums[i + 1] for all valid i.

思路：
    TODO

複雜度：
    Time: O(?)
    Space: O(?)
"""

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    # Test cases
    assert s.findPeakElement([1, 2, 3, 1]) == 2, "Case 1: simple peak in middle"
    result = s.findPeakElement([1, 2, 1, 3, 5, 6, 4])
    assert result in (1, 5), f"Case 2: multiple peaks, got {result}"
    # Edge case: single element
    assert s.findPeakElement([1]) == 0, "Edge: single element"
    # Edge case: strictly increasing (peak at end)
    assert s.findPeakElement([1, 2, 3, 4, 5]) == 4, "Edge: strictly increasing"
    # Edge case: strictly decreasing (peak at start)
    assert s.findPeakElement([5, 4, 3, 2, 1]) == 0, "Edge: strictly decreasing"
    print("All tests passed!")
