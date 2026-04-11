"""
LeetCode 230. Kth Smallest Element in a BST
Difficulty: Medium
Tags: Tree, BST, DFS, Inorder
URL: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

思路：
    透過 inorder 從最小值開始查找

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
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        count = k
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
                
            node = stack.pop()
            count -= 1
            if count == 0:
                return node.val


            curr = node.right

            
            


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
