"""
LeetCode 236. Lowest Common Ancestor of a Binary Tree
Difficulty: Medium
Tags: Tree
URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Problem:
    Given a binary tree, find the lowest common ancestor (LCA) of two given
    nodes in the tree.

    The lowest common ancestor is defined between two nodes p and q as the
    lowest node in the tree that has both p and q as descendants (where we
    allow a node to be a descendant of itself).

    Example 1:
        Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
        Output: 3
        Explanation: The LCA of nodes 5 and 1 is 3.

    Example 2:
        Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
        Output: 5
        Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a
                     descendant of itself according to the LCA definition.

    Example 3:
        Input: root = [1,2], p = 1, q = 2
        Output: 1

    Constraints:
        - The number of nodes in the tree is in the range [2, 10^5].
        - -10^9 <= Node.val <= 10^9
        - All Node.val are unique.
        - p != q
        - p and q will exist in the tree.

思路：
    這題是 Binary Tree，所以沒有辦法透過 Binary Search Tree 的特色加速查詢。

    主要邏輯如下：
    1. 如果當前的節點就等於 p 或 q 的話，就直接回傳。
    2. 如果左右兩條子樹都有回報的話，就直接回傳當前的 root。
    3. 如果只有回傳一邊，我就回傳那一邊就好。
    4. 空節點就回傳none

複雜度：
    Time: O(n) 最差全部走一便
    Space: O(h) h=樹高, 最差 O(n)
"""

from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        def dfs(n):
            if not n:
                return None
            
            if p == n or q == n:
                return n
            
            resL = dfs(n.left)
            resR = dfs(n.right)
            if resL and resR:
                return n
            return resL if resL else resR
    
        return dfs(root)
        


def build_tree_from_level(values):
    """Helper: build tree from level-order list with None for missing nodes."""
    if not values:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def find(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    return find(root.left, val) or find(root.right, val)


if __name__ == "__main__":
    s = Solution()

    # Example 1: tree = [3,5,1,6,2,0,8,null,null,7,4], p=5, q=1 → LCA=3
    root = build_tree_from_level([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p, q = find(root, 5), find(root, 1)
    assert s.lowestCommonAncestor(root, p, q).val == 3, "Case 1"

    # Example 2: same tree, p=5, q=4 → LCA=5 (node can be its own ancestor)
    p, q = find(root, 5), find(root, 4)
    assert s.lowestCommonAncestor(root, p, q).val == 5, "Case 2 (ancestor is p)"

    p, q = find(root, 6), find(root, 0)
    assert s.lowestCommonAncestor(root, p, q).val == 3, "Case 4 "
    # Example 3: minimal tree [1,2], p=1, q=2 → LCA=1
    root = build_tree_from_level([1, 2])
    p, q = find(root, 1), find(root, 2)
    assert s.lowestCommonAncestor(root, p, q).val == 1, "Case 3 (two-node)"

    print("All tests passed!")

    #      3
    #    5   1
    #   6 2 0 8
    #  NN74
