"""
LeetCode 236. Lowest Common Ancestor of a Binary Tree
Difficulty: Medium
Tags: Tree, DFS, Recursion, Post-order
URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

思路：
    {TODO: post-order recursion，base case + 左右子樹回報 + 決策}

複雜度：
    Time: O(n) n = 節點數
    Space: O(h) h = 樹深
"""

from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def postorder(node):
            if node is None or node == p or node == q:
                return node
            
            resL = postorder(node.left)
            resR = postorder(node.right)
            if resL and resR:
                return node

            return resR or resL

        return postorder(root)



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

    # Example 3: minimal tree [1,2], p=1, q=2 → LCA=1
    root = build_tree_from_level([1, 2])
    p, q = find(root, 1), find(root, 2)
    assert s.lowestCommonAncestor(root, p, q).val == 1, "Case 3 (two-node)"

    print("All tests passed!")
