"""
LeetCode 994. Rotting Oranges
Difficulty: Medium
Tags: Array, Matrix
URL: https://leetcode.com/problems/rotting-oranges/

Problem:
    You are given an m x n grid where each cell can have one of three values:
        - 0 representing an empty cell,
        - 1 representing a fresh orange, or
        - 2 representing a rotten orange.

    Every minute, any fresh orange that is 4-directionally adjacent to a
    rotten orange becomes rotten.

    Return the minimum number of minutes that must elapse until no cell has a
    fresh orange. If this is impossible, return -1.

    Example 1:
        Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
        Output: 4

    Example 2:
        Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
        Output: -1
        Explanation: The orange in the bottom left corner (row 2, column 0) is
        never rotten, because rotting only happens 4-directionally.

    Example 3:
        Input: grid = [[0,2]]
        Output: 0
        Explanation: Since there are already no fresh oranges at minute 0, the
        answer is just 0.

    Constraints:
        - m == grid.length
        - n == grid[i].length
        - 1 <= m, n <= 10
        - grid[i][j] is 0, 1, or 2.

思路：
    TODO（學生自己填；中文 OK）

複雜度：
    Time: O(m*n)
    Space: O(m*n)
"""

from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        counter = 0
        m, n = len(grid), len(grid[0])
        ways = [1, 0, -1, 0, 1]
        tmp = deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    counter += 1
                elif grid[i][j] == 2:
                    tmp.append((i, j))
        if counter == 0:
            return 0
        
        minutes = -1
        
        while tmp:
            tmpLen = len(tmp)
            minutes += 1
            for _ in range(tmpLen):
                r, c = tmp.popleft()
                for k in range(4):
                    nr, nc = r+ways[k] , c+ways[k+1]
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        counter -= 1
                        tmp.append((nr, nc))
        return -1 if counter != 0 else minutes


if __name__ == "__main__":
    s = Solution()
    # Test cases
    assert s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4, "Case 1"
    assert s.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1, "Case 2"
    assert s.orangesRotting([[0, 2]]) == 0, "Case 3"
    # Edge case
    assert s.orangesRotting([[0]]) == 0, "Edge: no oranges"
    assert s.orangesRotting([[1,1], [0, 1]]) == -1, "Edge: no rotten oranges"
    print("All tests passed!")
