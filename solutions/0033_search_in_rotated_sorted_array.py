"""
LeetCode 33. Search in Rotated Sorted Array
Difficulty: Medium
Tags: Array
URL: https://leetcode.com/problems/search-in-rotated-sorted-array/

Problem:
    There is an integer array nums sorted in ascending order (with distinct
    values).

    Prior to being passed to your function, nums is possibly rotated at an
    unknown pivot index k (1 <= k < nums.length) such that the resulting array
    is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
    (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index
    3 and become [4,5,6,7,0,1,2].

    Given the array nums after the possible rotation and an integer target,
    return the index of target if it is in nums, or -1 if it is not in nums.

    You must write an algorithm with O(log n) runtime complexity.

    Example 1:
        Input: nums = [4,5,6,7,0,1,2], target = 0
        Output: 4

    Example 2:
        Input: nums = [4,5,6,7,0,1,2], target = 3
        Output: -1

    Example 3:
        Input: nums = [1], target = 0
        Output: -1

    Constraints:
        - 1 <= nums.length <= 5000
        - -10^4 <= nums[i] <= 10^4
        - All values of nums are unique.
        - nums is an ascending array that is possibly rotated.
        - -10^4 <= target <= 10^4

思路：
    透過對半切 會有一邊排序另一邊無序 透過判斷mid和right的大小 可以知道哪一邊是有序, 在移動指標時, 可以先判斷 等號成立的狀況, 後續移動指標會單純一點

複雜度：
    Time: O(log(n))
    Space: O(1)
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = l + (r-l)//2
            mid = nums[m]
            
            if mid == target:
                return m
            # 左側排序
            if mid > nums[r]:
                if mid > target >= nums[l]:
                    r = m-1
                else:
                    l = m+1
            else: # 右側排序
                if mid < target <=nums[r]:
                    l = m+1
                else:
                    r = m-1
        return -1



if __name__ == "__main__":
    s = Solution()

    # Case 1: target in right (rotated) half
    assert s.search([4, 5, 6, 7, 0, 1, 2], 0) == 4, "Case 1"

    # Case 2: target not present
    assert s.search([4, 5, 6, 7, 0, 1, 2], 3) == -1, "Case 2"

    # Case 3: target in left (sorted) half
    assert s.search([4, 5, 6, 7, 0, 1, 2], 5) == 1, "Case 3"

    # Case 4: not rotated (k=0 effectively)
    assert s.search([1, 2, 3, 4, 5], 3) == 2, "Case 4: no rotation"

    # Edge case: single element
    assert s.search([1], 0) == -1, "Edge: single element not found"
    assert s.search([1], 1) == 0, "Edge: single element found"

    # 邊界：target 落在 nums[r] 或 nums[l]（外側邊界值要 <= 不能 <）
    assert s.search([4, 5, 6, 7, 0, 1, 2], 2) == 6, "Edge: target == nums[right]"
    assert s.search([4, 5, 6, 7, 0, 1, 2], 4) == 0, "Edge: target == nums[left]"

    print("All tests passed!")
