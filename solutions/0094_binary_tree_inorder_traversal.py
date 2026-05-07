"""
LeetCode 94. Binary Tree Inorder Traversal
Difficulty: Easy
Tags: Tree
URL: https://leetcode.com/problems/binary-tree-inorder-traversal/

Problem:
    Given the root of a binary tree, return the inorder traversal of its
    nodes' values.

    Example 1:
        Input: root = [1, null, 2, 3]
            1
             \\
              2
             /
            3
        Output: [1, 3, 2]

    Example 2:
        Input: root = []
        Output: []

    Example 3:
        Input: root = [1]
        Output: [1]

    Constraints:
        - The number of nodes in the tree is in the range [0, 100].
        - -100 <= Node.val <= 100

    Follow up:
        Recursive solution is trivial. Could you do it iteratively?

思路：
    使用stack將節點左側節點推入, 直到走到分支盡頭後, 再pop stack, 訪問root , 此時已經確認左子樹被走完了, 所以可以安心訪問右側

複雜度：
    Time: O(n) 每個點
    Space: O(h) h = 樹高 skewed tree => 節點數
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        curr = root
        ans = []

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            lastNode = stack.pop()
            ans.append(lastNode.val)
            curr = lastNode.right
        return ans


if __name__ == "__main__":
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

    # Case 1: [1, null, 2, 3] -> [1, 3, 2]
    root1 = build_tree([1, None, 2, None, None, 3])
    assert Solution().inorderTraversal(root1) == [1, 3, 2], "Case 1"

    # Case 2: empty tree
    assert Solution().inorderTraversal(None) == [], "Case 2: empty"

    # Case 3: single node
    root3 = build_tree([1])
    assert Solution().inorderTraversal(root3) == [1], "Case 3: single"

    # Case 4: balanced [5, 3, 6, 2, 4] -> [2, 3, 4, 5, 6]
    root4 = build_tree([5, 3, 6, 2, 4])
    assert Solution().inorderTraversal(root4) == [2, 3, 4, 5, 6], "Case 4"

    # Case 5: left chain only [3, 2, None, 1] -> [1, 2, 3]
    root5 = build_tree([3, 2, None, 1])
    assert Solution().inorderTraversal(root5) == [1, 2, 3], "Case 5: left chain"

    print("All tests passed!")
