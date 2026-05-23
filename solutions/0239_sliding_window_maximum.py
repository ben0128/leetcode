"""
LeetCode 239. Sliding Window Maximum
Difficulty: Hard
Tags: Array
URL: https://leetcode.com/problems/sliding-window-maximum/

Problem:
    You are given an array of integers nums, there is a sliding window of size k
    which is moving from the very left of the array to the very right. You can
    only see the k numbers in the window. Each time the sliding window moves
    right by one position.

    Return the max sliding window.

    Example 1:
        Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
        Output: [3,3,5,5,6,7]
        Explanation:
            Window position                Max
            ---------------               -----
            [1  3  -1] -3  5  3  6  7       3
             1 [3  -1  -3] 5  3  6  7       3
             1  3 [-1  -3  5] 3  6  7       5
             1  3  -1 [-3  5  3] 6  7       5
             1  3  -1  -3 [5  3  6] 7       6
             1  3  -1  -3  5 [3  6  7]      7

    Example 2:
        Input: nums = [1], k = 1
        Output: [1]

    Constraints:
        - 1 <= nums.length <= 10^5
        - -10^4 <= nums[i] <= 10^4
        - 1 <= k <= nums.length

思路：
    先準備一個遞減的 monotonic queue：
Deque 內的元素滿足：(1) nums[index] 單調遞減，(2) 所有 index 都在 [i-k+1, i] 內。
1. 每當進入新視窗時，先檢查第一個元素是否還在窗內，如果不在的話就執行 popleft
2. 檢查佇列末端的元素一定要比新元素大，否則就持續 pop 最後一個元素，直到 queue 為空或是滿足條件為止
3. 檢查完成之後，就抓取這個 queue 裡面的第一個，即為 temporary 的 maximum。
複雜度：
    Time: O(n)
    Space: O(k)
"""
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        monoQueue = deque([])
        n = len(nums)

        ans = [0] * (n-k+1)
        # start loop
        for i in range(n):
            left = i-k+1
            if monoQueue and monoQueue[0] < left:
                monoQueue.popleft()
            while monoQueue and nums[monoQueue[-1]] < nums[i]:
                monoQueue.pop()
            monoQueue.append(i)
            if left >= 0:
                ans[left] = nums[monoQueue[0]]
                
        return ans


if __name__ == "__main__":
    s = Solution()

    # Test case 1: nums=[1,3,-1,-3,5,3,6,7], k=3 -> [3,3,5,5,6,7]
    assert s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7], "Case 1"

    # Test case 2: single element window
    assert s.maxSlidingWindow([1], 1) == [1], "Case 2: single"

    # Test case 3: k equals array length
    assert s.maxSlidingWindow([1,3,2], 3) == [3], "Case 3: k=n"

    # Test case 4: decreasing array
    assert s.maxSlidingWindow([5,4,3,2,1], 3) == [5,4,3], "Case 4: decreasing"

    # Test case 5: increasing array
    assert s.maxSlidingWindow([1,2,3,4,5], 3) == [3,4,5], "Case 5: increasing"

    # Test case 6: duplicates
    assert s.maxSlidingWindow([1,1,1,1], 2) == [1,1,1], "Case 6: all duplicates"

    # Test case 7: k=1 (window of size 1)
    assert s.maxSlidingWindow([4,2,7,1,5], 1) == [4,2,7,1,5], "Case 7: k=1"

    print("All tests passed!")
