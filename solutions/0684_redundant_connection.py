"""
LeetCode 684. Redundant Connection
Difficulty: Medium
Tags: Graph
URL: https://leetcode.com/problems/redundant-connection/

Problem:
    In this problem, a tree is an undirected graph that is connected and
    has no cycles.

    You are given a graph that started as a tree with n nodes labeled from
    1 to n, with one additional edge added. The added edge has two
    different vertices chosen from 1 to n, and was not an edge that already
    existed. The graph is represented as an array edges of length n where
    edges[i] = [ai, bi] indicates that there is an edge between nodes ai
    and bi in the graph.

    Return an edge that can be removed so that the resulting graph is a tree
    of n nodes. If there are multiple answers, return the answer that occurs
    last in the input.

    Example 1:
        Input: edges = [[1,2],[1,3],[2,3]]
        Output: [2,3]

    Example 2:
        Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
        Output: [1,4]

    Constraints:
        - n == edges.length
        - 3 <= n <= 1000
        - edges[i].length == 2
        - 1 <= ai < bi <= n
        - ai != bi
        - There are no repeated edges.
        - The given graph is connected and has exactly one cycle
          (i.e., it is a tree plus one extra edge).

思路：
    uf 連結node 將node分組, 並透過roots 和ranks 加速查找, 根據此題的作法只會有一組邊形成circle 所以可以提早return
    當發現兩個點root 相同時, 如果我再次union 就會形成circle 所以這次可以直接return

複雜度：
    n = edges長度
    Time: O(n) 
    Space: O(n)
"""

from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 0,1,2..., n  (首項用不到)
        m = len(edges)
        roots = [i for i in range(m+1)]
        ranks = [0] * (m+1)
        def find(n):
            curr = n
            while curr != roots[curr]:
                roots[curr] = roots[roots[curr]]
                curr = roots[curr]
            return curr
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return [x, y]

            if ranks[rootX] > ranks[rootY]:
                roots[rootY] = roots[rootX]
            elif ranks[rootX] < ranks[rootY]:
                roots[rootX] = roots[rootY]
            else:
                roots[rootX] = roots[rootY]
                ranks[rootY] += 1
            return None
        
        for x, y in edges:
            if union(x, y) is not None:
                return [x, y]


if __name__ == "__main__":
    sol = Solution()

    # Test cases
    assert sol.findRedundantConnection([[1, 2], [1, 3], [2, 3]]) == [2, 3], "Case 1"
    assert sol.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4], "Case 2"

    # Edge: the cycle-closing edge is the very last one
    assert sol.findRedundantConnection([[1, 2], [2, 3], [3, 1]]) == [3, 1], "Edge: last edge closes cycle"
    assert sol.findRedundantConnection([[1, 2], [1, 3], [2, 3], [1, 4]]) == [2, 3], "Edge: redundant in the middle, node = n"

    print("All tests passed!")
