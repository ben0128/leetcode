"""
LeetCode 235. Lowest Common Ancestor of a Binary Search Tree
Difficulty: Medium
Tags: Tree, BST, DFS
URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

思路：
    Using the features of a BST:
1. If the node is between the smaller and the bigger values, just return the node.
2. If not, use the features of the BST to find the better route.

複雜度：
    Time: O(n) 最差是skewed tree
    Space: O(1)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        small, big = p.val, q.val
        if small > big:
            small, big = big, small
        
        node = root
        while node:
            v = node.val
            if small <= v <= big:
                return node
            elif v > big: # root 比兩個點都大 => 往左
                node = node.left
            else: # root 比兩個點都大 => 往左
                node = node.right

        # small, big = p.val, q.val
        # if small > big:
        #     small, big = big, small
        # def lca(node):
        #     if small <= node.val <= big:
        #         return node
            
        #     if node.val > big:
        #         return lca(node.left)
        #     if node.val < small:
        #         return lca(node.right)

        # return lca(root)

if __name__ == "__main__":
    # Helper to build tree from list
    def build_tree(vals):
        if not vals:
            return None
        nodes = [TreeNode(v) if v is not None else None for v in vals]
        for i, node in enumerate(nodes):
            if node:
                left_idx = 2 * i + 1
                right_idx = 2 * i + 2
                if left_idx < len(nodes):
                    node.left = nodes[left_idx]
                if right_idx < len(nodes):
                    node.right = nodes[right_idx]
        return nodes[0]

    # Test case 1: root=[6,2,8,0,4,7,9,null,null,3,5], p=2, q=8 -> 6
    root1 = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p1, q1 = root1.left, root1.right  # p=2, q=8
    assert Solution().lowestCommonAncestor(root1, p1, q1).val == 6, "Case 1"

    # Test case 2: root=[6,2,8,0,4,7,9,null,null,3,5], p=2, q=4 -> 2
    p2, q2 = root1.left, root1.left.right  # p=2, q=4
    assert Solution().lowestCommonAncestor(root1, p2, q2).val == 2, "Case 2"

    # Edge case: p=3, q=5 -> 4
    p3, q3 = root1.left.right.left, root1.left.right.right  # p=3, q=5
    assert Solution().lowestCommonAncestor(root1, p3, q3).val == 4, "Edge case"

    print("All tests passed!")
