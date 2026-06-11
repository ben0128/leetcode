"""
LeetCode 235. Lowest Common Ancestor of a Binary Search Tree
Difficulty: Medium
Tags: Tree
URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Problem:
    Given a binary search tree (BST), find the lowest common ancestor (LCA) node of
    two given nodes p and q in the BST.

    The lowest common ancestor is defined between two nodes p and q as the lowest node
    in T that has both p and q as descendants (where we allow a node to be a descendant
    of itself).

    Example 1:
        Input:  root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
        Output: 6
        Explanation: The LCA of nodes 2 and 8 is 6.

    Example 2:
        Input:  root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
        Output: 2
        Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant
                     of itself according to the LCA definition.

    Example 3:
        Input:  root = [2,1], p = 2, q = 1
        Output: 2

    Constraints:
        - The number of nodes in the tree is in the range [2, 10^5].
        - -10^9 <= Node.val <= 10^9
        - All Node.val are unique.
        - p != q
        - p and q will exist in the BST.

思路：
    dfs to find target
    I use an iterative approach to find the nodes. If I find that the current node's value is between p and q, I just return current node.

However, if both nodes are greater or smaller than the root, I use the features of bst to change the root nodes .

複雜度：
    Time: O(h) h = 樹深 最差O(n)
    Space: O(1) 
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        # let p.val > q.val
        if p.val < q.val:
            p, q = q, p
        pval, qval = p.val, q.val

        while curr:
            currVal = curr.val
            if qval <= currVal <= pval:
                return curr
            
            if currVal < pval:
                curr = curr.right
            else:
                curr = curr.left
            




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

    # Test case 2: root=[6,2,8,0,4,7,9,null,null,3,5], p=2, q=4 -> 2 (node is descendant of itself)
    p2, q2 = root1.left, root1.left.right  # p=2, q=4
    assert Solution().lowestCommonAncestor(root1, p2, q2).val == 2, "Case 2"

    # Edge case: p=3, q=5 -> 4
    p3, q3 = root1.left.right.left, root1.left.right.right  # p=3, q=5
    assert Solution().lowestCommonAncestor(root1, p3, q3).val == 4, "Edge case"

    p4, q4 = root1, root1.left
    assert Solution().lowestCommonAncestor(root1, p4, q4).val == 6, "Edge case"
    print("All tests passed!")

#          6
#        2   8
#      0  4  7  9
#        3 5