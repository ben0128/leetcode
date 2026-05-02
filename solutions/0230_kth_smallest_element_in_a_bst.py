"""
LeetCode 230. Kth Smallest Element in a BST
Difficulty: Medium
Tags: Tree, BST, DFS, Inorder
URL: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Problem:
    Given the root of a binary search tree, and an integer k, return the kth
    smallest value (1-indexed) of all the values of the nodes in the tree.

    Example 1:
        Input: root = [3,1,4,null,2], k = 1
        Output: 1
        Tree:
                3
               / \
              1   4
               \
                2

    Example 2:
        Input: root = [5,3,6,2,4,null,null,1], k = 3
        Output: 3
        Tree:
                  5
                 / \
                3   6
               / \
              2   4
             /
            1

    Constraints:
        - The number of nodes in the tree is n.
        - 1 <= k <= n <= 10^4
        - 0 <= Node.val <= 10^4

    Follow up:
        If the BST is modified often (i.e., we can do insert and delete operations)
        and you need to find the kth smallest frequently, how would you optimize?

思路：
    Because this is a binary search tree, I can search from left, then root, then right. I will use this order to traverse the tree and find the kth smallest element.

複雜度：
    Time: O(n)
    Space: O(n) 
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.count = k
        def traversal(n):
            if not n:
                return
            
            resL = traversal(n.left)
            if resL:
                return resL
            self.count -= 1
            if self.count == 0:
                return n
            resR = traversal(n.right)
            if resR:
                return resR
            return 

        return traversal(root).val



if __name__ == "__main__":
    # Helper to build tree from list (level-order with None for missing children)
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

    # Test case 1: root=[3,1,4,null,2], k=1 -> 1
    root1 = build_tree([3, 1, 4, None, 2])
    assert Solution().kthSmallest(root1, 1) == 1, "Case 1"

    # Test case 2: root=[5,3,6,2,4,null,null,1], k=3 -> 3
    root2 = build_tree([5, 3, 6, 2, 4, None, None, 1])
    assert Solution().kthSmallest(root2, 3) == 3, "Case 2"

    # Edge case: k equals total number of nodes
    root3 = build_tree([3, 1, 4, None, 2])
    assert Solution().kthSmallest(root3, 4) == 4, "Edge case: k = n"

    print("All tests passed!")
