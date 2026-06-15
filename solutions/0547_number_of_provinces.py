"""
LeetCode 547. Number of Provinces
Difficulty: Medium
Tags: Graph
URL: https://leetcode.com/problems/number-of-provinces/

Problem:
    There are n cities. Some of them are connected, while some are not. If city a
    is connected directly with city b, and city b is connected directly with city c,
    then city a is connected indirectly with city c.

    A province is a group of directly or indirectly connected cities and no other
    cities outside of the group.

    You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith
    city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

    Return the total number of provinces.

    Example 1:
        Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
        Output: 2
        Explanation: Cities 0 and 1 form one province; city 2 forms another.

    Example 2:
        Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
        Output: 3
        Explanation: No connections — each city is its own province.

    Constraints:
        - 1 <= n <= 200
        - n == isConnected.length == isConnected[i].length
        - isConnected[i][j] is 1 or 0.
        - isConnected[i][i] == 1
        - isConnected[i][j] == isConnected[j][i]
"""


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        roots = [i for i in range(n)]
        ranks = [0] * n

        def find(node):
            while roots[node] != roots[roots[node]]:
                roots[node] = roots[roots[node]]
                node = roots[node]
            return roots[node]
        
        def union(x, y):
            rootX, rootY = find(x), find(y)

            if rootX != rootY:
                if ranks[rootX] < ranks[rootY]:
                    roots[rootX] = rootY
                elif ranks[rootY] < ranks[rootX]:
                    roots[rootY] = rootX
                else:
                    roots[rootY] = rootX
                    ranks[rootX] += 1
            return 
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    union(i, j)
        
        return len(set([find(i) for i in range(n)]))


if __name__ == "__main__":
    s = Solution()

    # Test case 1: cities 0,1 connected; city 2 alone -> 2
    assert s.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2, "Case 1"

    # Test case 2: no connections -> 3
    assert s.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3, "Case 2"

    # Test case 3: all connected -> 1
    assert s.findCircleNum([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 1, "Case 3"

    # Edge case: single city -> 1
    assert s.findCircleNum([[1]]) == 1, "Edge: single"

    print("All tests passed!")
