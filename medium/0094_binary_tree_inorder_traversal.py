"""
LeetCode 94. Binary Tree Inorder Traversal
Difficulty: Easy
Tags: Tree, DFS, Stack, Inorder
URL: https://leetcode.com/problems/binary-tree-inorder-traversal/

思路：
    透過 iteration 的 inorder 處理

複雜度：
    Time: O(n) n = 節點數
    Space: O(h) h = 樹高
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        stack = []
        curr = root
        ans = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            popEl = stack.pop()
            ans.append(popEl.val)

            curr = popEl.right
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

    # Test case 1: [1,null,2,3] -> [1,3,2]
    root1 = build_tree([1, None, 2, None, None, 3])
    assert Solution().inorderTraversal(root1) == [1, 3, 2], "Case 1"

    # Test case 2: empty tree -> []
    assert Solution().inorderTraversal(None) == [], "Case 2: empty"

    # Test case 3: single node [1] -> [1]
    root3 = build_tree([1])
    assert Solution().inorderTraversal(root3) == [1], "Case 3: single"

    # Test case 4: [5,3,6,2,4] -> [2,3,4,5,6]
    root4 = build_tree([5, 3, 6, 2, 4])
    assert Solution().inorderTraversal(root4) == [2, 3, 4, 5, 6], "Case 4"

    print("All tests passed!")
