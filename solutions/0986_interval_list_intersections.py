"""
LeetCode 986. Interval List Intersections
Difficulty: Medium
Tags: Array
URL: https://leetcode.com/problems/interval-list-intersections/

Problem:
    You are given two lists of closed intervals, firstList and secondList, where
    firstList[i] = [start_i, end_i] and secondList[j] = [start_j, end_j].

    Each list of intervals is pairwise disjoint and sorted in ascending order by start.

    Return the intersection of these two interval lists.

    A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

    The intersection of two closed intervals is a set of real numbers that are either
    empty or represented as a closed interval. For example, the intersection of
    [1, 3] and [2, 4] is [2, 3].

    Example 1:
        Input:  firstList  = [[0,2],[5,10],[13,23],[24,25]]
                secondList = [[1,5],[8,12],[15,24],[25,26]]
        Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

    Example 2:
        Input:  firstList = [[1,3],[5,9]], secondList = []
        Output: []

    Constraints:
        - 0 <= firstList.length, secondList.length <= 1000
        - firstList.length + secondList.length >= 1
        - 0 <= start_i < end_i <= 10^9
        - end_i < start_(i+1)   (within a list, intervals are disjoint and sorted)

思路：
    我想用雙指針init各指在兩組index = 0, 兩組會有兩種可能:有交集或是沒交集, 如果沒交集就移動end比較小的那邊的index如果有交集就找出交集範圍 
    , 並且記在外面並移動end比較小的index

複雜度：
    m, n = 兩陣列長度
    Time: O(m+n)
    Space: O(m+n)
"""

from typing import List


class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        ans = []
        fLen , sLen = len(firstList), len(secondList)
        # 4, 4
        if fLen == 0 or sLen == 0:
            return ans
        
        f, s = 0, 0
        # 1, 0 
        while f < fLen and s < sLen:
            fS, fE = firstList[f]
            sS, sE = secondList[s]
            tmpS, tmpE = max(fS, sS), min(fE, sE)
                
            if tmpS <= tmpE:
                ans.append([tmpS, tmpE])

            if fE > sE:
                s += 1
            else:
                f += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    # Case 1 — main example (note the single-point intersections [5,5], [24,24], [25,25])
    assert s.intervalIntersection(
        [[0, 2], [5, 10], [13, 23], [24, 25]],
        [[1, 5], [8, 12], [15, 24], [25, 26]],
    ) == [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]], "Case 1"

    # Case 2 — simple single overlap
    assert s.intervalIntersection([[1, 7]], [[3, 10]]) == [[3, 7]], "Case 2"

    # Edge case — one list is empty
    assert s.intervalIntersection([], [[1, 5]]) == [], "Edge: empty list"
    assert s.intervalIntersection([[1, 2], [3, 4]], [[2, 3], [4, 6]]) == [[2,2], [3, 3], [4, 4]], "single node answer"

    print("All tests passed!")
