"""
LeetCode 64. Minimum Path Sum
Difficulty: Medium
Tags: Dynamic Programming, 2D DP, Grid
URL: https://leetcode.com/problems/minimum-path-sum/

思路：
    DP 定義是從起點走到當前位置的每一條路徑的最小值。
    轉移方程考慮從上面來的路徑，和左邊來的那條路徑，特別去加總當前位置的值，選小的那條路徑。
    Base case 就是 grid[0][0]的值

複雜度：
    Time: O(m*n) 每一格都要走
    Space: O(n) row長度
"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        
        for i in range(1, m):
            row = grid[i]
            grid[i][0] += grid[i-1][0]
            
            for j in range(1, n):
                row[j] = min(grid[i-1][j], row[j-1]) + row[j]
        return grid[-1][-1]


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
    print("All tests passed!")
