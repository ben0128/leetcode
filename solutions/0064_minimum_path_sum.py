"""
LeetCode 64. Minimum Path Sum
Difficulty: Medium
Tags: Array, Matrix
URL: https://leetcode.com/problems/minimum-path-sum/

Problem:
    Given a m x n grid filled with non-negative numbers, find a path from top left
    to bottom right, which minimizes the sum of all numbers along its path.

    Note: You can only move either down or right at any point in time.

    Example 1:
        Input:  grid = [[1,3,1],[1,5,1],[4,2,1]]
        Output: 7
        Explanation: Because the path 1 -> 3 -> 1 -> 1 -> 1 minimizes the sum.

    Example 2:
        Input:  grid = [[1,2,3],[4,5,6]]
        Output: 12

    Constraints:
        - m == grid.length
        - n == grid[i].length
        - 1 <= m, n <= 200
        - 0 <= grid[i][j] <= 200

思路：
    I will use dynamic programming because I need to find the minimum path sum. 
    In every cell, I need to consider the direction: from the top or from the left and choose the minimum one.
    Finally, I'll just return the bottom-right cell.
    我站在 cell 的時候，準備計算時，我上方的格子和左邊的格子都已經是各自的最小值。所以我只要再去比較一次這兩條路線的最小值，並加到我身上，就可以計算出我的最小值了
複雜度：
    Time: O(m*n)
    Space: O(1) In-place modification, so don't need extra space.
"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[m-1][n-1]


if __name__ == "__main__":
    s = Solution()
    # Example 1
    assert s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7, "Case 1"
    # Example 2
    assert s.minPathSum([[1, 2, 3], [4, 5, 6]]) == 12, "Case 2"
    # Edge: single cell
    assert s.minPathSum([[5]]) == 5, "Single cell"
    # Edge: single row
    assert s.minPathSum([[1, 2, 3]]) == 6, "Single row"
    # Edge: single column
    assert s.minPathSum([[1], [2], [3]]) == 6, "Single column"
    
    assert s.minPathSum([[0, 0], [1, 0], [199, 0]]) == 0, "zeros "
    print("All tests passed!")
