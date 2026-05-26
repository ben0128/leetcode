"""
LeetCode 525. Contiguous Array
Difficulty: Medium
Tags: Array, Hash Table
URL: https://leetcode.com/problems/contiguous-array/

Problem:
    Given a binary array nums, return the maximum length of a contiguous
    subarray with an equal number of 0 and 1.

    Example 1:
        Input: nums = [0, 1]
        Output: 2
        Explanation: [0, 1] is the longest contiguous subarray with an
        equal number of 0 and 1.

    Example 2:
        Input: nums = [0, 1, 0]
        Output: 2
        Explanation: [0, 1] (or [1, 0]) is the longest contiguous subarray
        with equal number of 0 and 1.

    Example 3:
        Input: nums = [0, 1, 1, 1, 1, 1, 0, 0, 0]
        # preflixsum= [-1,0, 1, 2, 3, 4, 3, 2, 1]
        Output: 6
        Explanation: [1, 1, 1, 0, 0, 0] is the longest contiguous subarray
        with equal number of 0 and 1.

    Constraints:
        - 1 <= nums.length <= 10^5
        - nums[i] is either 0 or 1.

思路：
    1. 演算法骨架：
        (a) Transform：0→-1, 1→+1（讓「0/1 數量相等」變成「subarray 和為 0」）
        (b) 一邊遍歷一邊累加 prevSum；hashmap 沒見過此值就存 (prevSum→i)，
            見過就用 i - hashmap[prevSum] 更新 ans
    2. 資料結構 + 理由：hashmap {prefix sum 值: 最早出現的 index}。
        value 存「最早 index」是因為要算「最長」subarray (length = curr_i - earliest_i)；
        hashmap O(1) 查「這個 prefix sum 之前出現過嗎、在哪？」
    3. Invariant（迴圈尾，處理完 index i 後）：
        (1) 對 hashmap 任意 entry (v, idx)：idx 是 prevSum 第一次達到 v 的 index
        (2) ans = 截至目前所有「和為 0 子陣列」的最大長度
    4. 複雜度：Time O(n)；Space O(n)（hashmap 最多 n+1 entries——單次執行下 prevSum 至多 n+1 個 snapshot）

複雜度：
    Time: O(n) n = len(nums)
    Space: O(n) hashmap 最多 n+1 entries
"""

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prevSum = 0
        hashMap = { 0:-1 }
        ans = 0
        for i, num in enumerate(nums):
            prevSum += 1 if num == 1 else -1

            if prevSum not in hashMap:
                hashMap[prevSum] = i
            else:
                ans = max(i - hashMap[prevSum], ans)
        return ans


if __name__ == "__main__":
    sol = Solution()
    # Test cases
    assert sol.findMaxLength([0, 1]) == 2, "Case 1"
    assert sol.findMaxLength([0, 1, 0]) == 2, "Case 2"
    assert sol.findMaxLength([0, 1, 1, 1, 1, 1, 0, 0, 0]) == 6, "Case 3"
    # Edge cases
    assert sol.findMaxLength([0]) == 0, "Single zero"
    assert sol.findMaxLength([1, 1, 1, 1]) == 0, "All ones"
    assert sol.findMaxLength([0, 0, 1, 0, 0, 0, 1, 1]) == 6, "Wraps non-zero start"
    print("All tests passed!")
