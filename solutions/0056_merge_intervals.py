"""
LeetCode 56. Merge Intervals
Difficulty: Medium
Tags: Array
URL: https://leetcode.com/problems/merge-intervals/

Problem:
    Given an array of intervals where intervals[i] = [start_i, end_i],
    merge all overlapping intervals, and return an array of the
    non-overlapping intervals that cover all the intervals in the input.

    Example 1:
        Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
        Output: [[1,6],[8,10],[15,18]]
        Explanation: Since intervals [1,3] and [2,6] overlap, merge them
        into [1,6].

    Example 2:
        Input: intervals = [[1,4],[4,5]]
        Output: [[1,5]]
        Explanation: Intervals [1,4] and [4,5] are considered overlapping.

    Constraints:
        - 1 <= intervals.length <= 10^4
        - intervals[i].length == 2
        - 0 <= start_i <= end_i <= 10^4

思路：
    - 4-段：演算法骨架 / 資料結構+理由 / Invariant(狀態) / 複雜度
    先根據start => end 排序, 並且過程中將重疊部分merge成一個(要比對當前end 和新的end 誰比較大),end 會是 到目前為止所有看過的區間的 最大值, 當發現沒有 overlap 就推入 ans 
    用list 就能, 無法使用binary search 因為 前一個的end 可能會比後一個 end 還大 所以不能跳過中間的區間
    

複雜度：
    Time: O(n * log(n))
    Space: O(n)
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        currWindow = [intervals[0][0], intervals[0][1]]
        n = len(intervals)
        for i in range(1, n):
            start, end = intervals[i]
            if start <= currWindow[1]:
                currWindow[1] = max(currWindow[1], end)
            else:
                ans.append(currWindow.copy())
                currWindow = [start, end]
        ans.append(currWindow)
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Test cases
    assert sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]], "Case 1"
    assert sol.merge([[1, 4], [4, 5]]) == [[1, 5]], "Case 2 (touching)"

    # Edge: single interval
    assert sol.merge([[1, 4]]) == [[1, 4]], "Edge: single"

    # Edge: input not sorted by start
    assert sol.merge([[2, 6], [1, 3]]) == [[1, 6]], "Edge: unsorted input"

    
    # 事後 gate：在這行下面加 >=1 個你自己想的 case（不能是上面的變體）
    assert sol.merge([[1, 8], [2, 6]]) == [[1, 8]], "Case 4"
    # assert ...

    print("All tests passed!")
