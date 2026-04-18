"""
LeetCode 547. Number of Provinces
Difficulty: Medium
Tags: Graph, Union Find, DFS
URL: https://leetcode.com/problems/number-of-provinces/

思路：
    Use Union-Find to connect the new nodes and calculate the number of different nodes that connect to each other.

複雜度：
    Time: O(n^2) n = 節點數
    Space: O(n) 
"""


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        roots = [i for i in range(n)]
        ranks = [0 for _ in range(n)]
        def find(node):
            while roots[node] != roots[roots[node]]:
                roots[node] = roots[roots[node]]
            return roots[node]

        def union(x, y):
            rootX, rootY = find(x), find(y)

            if rootX != rootY:
                if ranks[rootX] < ranks[rootY]:
                    roots[rootX] = rootY
                elif ranks[rootX] > ranks[rootY]:
                    roots[rootY] = rootX
                else:
                    roots[rootY] = rootX
                    ranks[rootX] += 1
            return
        
        for i in range(n):
            for j in range(n):
                if i > j and isConnected[i][j] == 1:
                    union(i, j)
        
        ans = set()
        for root in roots:
            ans.add(find(root))
        return len(ans)



if __name__ == "__main__":
    s = Solution()

    # Test case 1: [[1,1,0],[1,1,0],[0,0,1]] -> 2
    # Cities 0,1 are connected; city 2 is alone
    assert s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]) == 2, "Case 1"

    # Test case 2: [[1,0,0],[0,1,0],[0,0,1]] -> 3
    # No connections, each city is its own province
    assert s.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]) == 3, "Case 2"

    # Test case 3: [[1,1,1],[1,1,1],[1,1,1]] -> 1
    # All connected
    assert s.findCircleNum([[1,1,1],[1,1,1],[1,1,1]]) == 1, "Case 3"

    # Edge case: single city
    assert s.findCircleNum([[1]]) == 1, "Edge: single"

    print("All tests passed!")
