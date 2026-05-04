"""
LeetCode 973. K Closest Points to Origin
Difficulty: Medium
Tags: Array, Math
URL: https://leetcode.com/problems/k-closest-points-to-origin/

Problem:
    Given an array of points where points[i] = [xi, yi] represents a point on
    the X-Y plane and an integer k, return the k closest points to the origin
    (0, 0).

    The distance between two points on the X-Y plane is the Euclidean distance
    (i.e., sqrt((x1 - x2)^2 + (y1 - y2)^2)).

    You may return the answer in any order. The answer is guaranteed to be
    unique (except for the order that it is in).

    Example 1:
        Input: points = [[1,3],[-2,2]], k = 1
        Output: [[-2,2]]
        Explanation:
            The distance between (1, 3) and the origin is sqrt(10).
            The distance between (-2, 2) and the origin is sqrt(8).
            Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
            We only want the closest k = 1 points from the origin, so the
            answer is just [[-2,2]].

    Example 2:
        Input: points = [[3,3],[5,-1],[-2,4]], k = 2
        Output: [[3,3],[-2,4]]
        Explanation: The answer [[-2,4],[3,3]] would also be accepted.

    Constraints:
        - 1 <= k <= points.length <= 10^4
        - -10^4 <= xi, yi <= 10^4

    Follow up:
        Could you solve it in better than O(n log n) time?

思路：
    use max heap to find close point

複雜度：
    k = input number, n = points 長度
    Time: O(nlog(k))
    Space: O(k)
"""

from typing import List
from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxH = []
        for i, [x,y] in enumerate(points):
            dis = x ** 2 + y ** 2
            heappush(maxH, (-dis, i))
            if len(maxH) > k:
                heappop(maxH)
        return [points[idx] for dis, idx in maxH]


if __name__ == "__main__":
    s = Solution()

    # Case 1: k=1
    result1 = s.kClosest([[1, 3], [-2, 2]], 1)
    assert result1 == [[-2, 2]], f"Case 1 failed: {result1}"

    # Case 2: k=2 (any order)
    result2 = s.kClosest([[3, 3], [5, -1], [-2, 4]], 2)
    assert sorted(result2) == sorted([[3, 3], [-2, 4]]), f"Case 2 failed: {result2}"

    # Case 3: k equals all points
    result3 = s.kClosest([[1, 1], [2, 2], [3, 3]], 3)
    assert sorted(result3) == sorted([[1, 1], [2, 2], [3, 3]]), f"Case 3 failed: {result3}"

    # Edge case: single point, k=1
    result4 = s.kClosest([[0, 1]], 1)
    assert result4 == [[0, 1]], f"Edge case failed: {result4}"

    print("All tests passed!")
