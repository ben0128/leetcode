"""
LeetCode 239. Sliding Window Maximum
Difficulty: Hard
Tags: Array, Queue, Sliding Window, Monotonic Queue
URL: https://leetcode.com/problems/sliding-window-maximum/

思路：
    透過 Monotonics queue 快速查找視窗內的最大值

複雜度：
    Time: O(N)
    Space: O(k)
"""
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        queue = deque([])

        for idx in range(k):
            while queue and queue[-1][0] < nums[idx]:
                queue.pop()
            queue.append([nums[idx], idx])
        
        ans = []
        n = len(nums)
        for idx in range(len(nums)-k+1):
            while idx > queue[0][1]:
                queue.popleft()
            
            ans.append(queue[0][0])

            if idx+k < n:
                num = nums[idx+k]
                while queue and queue[-1][0] < num:
                    queue.pop()
                queue.append([num, idx+k])
        
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

    print("All tests passed!")
