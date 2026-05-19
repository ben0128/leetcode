"""
LeetCode 153. Find Minimum in Rotated Sorted Array
Difficulty: Medium
Tags: Array
URL: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Problem:
    Suppose an array of length n sorted in ascending order is rotated between
    1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
        - [4,5,6,7,0,1,2] if it was rotated 4 times.
        - [0,1,2,4,5,6,7] if it was rotated 7 times.

    Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results
    in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

    Given the sorted rotated array nums of unique elements, return the minimum
    element of this array.

    You must write an algorithm that runs in O(log n) time.

    Example 1:
        Input: nums = [3,4,5,1,2]
        Output: 1
        Explanation: The original array was [1,2,3,4,5] rotated 3 times.

    Example 2:
        Input: nums = [4,5,6,7,0,1,2]
        Output: 0
        Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

    Example 3:
        Input: nums = [11,13,15,17]
        Output: 11
        Explanation: The original array was [11,13,15,17] and it was rotated 4 times.

    Constraints:
        - n == nums.length
        - 1 <= n <= 5000
        - -5000 <= nums[i] <= 5000
        - All the integers of nums are unique.
        - nums is sorted and rotated between 1 and n times.

思路：
    將mid和r去比, 如果mid > r 就代表左側有序 所以留右側 l = mid+1
    反之, 就會需要 r = mid
    如果是用mid和l比,會在 [1, 2, 3] 切錯邊
    nums[mid] vs nums[r]：
    分支 1: 若 nums[mid] > nums[r] → min 在 __右__ 半邊 → l = __mid+1__
    分支 2: 若 nums[mid] < nums[r] → min 在 __左__ 半邊 → r = __mid__

複雜度：
    Time: O(log(len(nums)))
    Space: O(1)
"""


class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l < r:
            m = (l+r) // 2
            # 左邊有排序
            if nums[m] > nums[r]:
                l = m+1
            else: # 右邊有排序
                r = m
        return nums[l]
    
# A: (l, m, r) = (0, 2, 4) => (3, 3, 4) => (3, 3, 3)
# B: (l, m, r) = (0, 1, 2) => (0, 0, 1) => (0, 0, 0)



if __name__ == "__main__":
    sol = Solution()
    # Test cases
    assert sol.findMin([3, 4, 5, 1, 2]) == 1, "Case 1: pivot in middle"
    assert sol.findMin([4, 5, 6, 7, 0, 1, 2]) == 0, "Case 2: pivot late"
    assert sol.findMin([11, 13, 15, 17]) == 11, "Case 3: not rotated (full rotation)"
    # Edge cases
    assert sol.findMin([1]) == 1, "Edge: single element"
    assert sol.findMin([2, 1]) == 1, "Edge: two elements rotated"
    assert sol.findMin([1, 2]) == 1, "Edge: two elements not rotated"
    print("All tests passed!")
