"""
LeetCode 124. Binary Tree Maximum Path Sum
Difficulty: Hard
Tags: Tree
URL: https://leetcode.com/problems/binary-tree-maximum-path-sum/

Problem:
    A path in a binary tree is a sequence of nodes where each pair of adjacent
    nodes in the sequence has an edge connecting them. A node can only appear
    in the sequence at most once. Note that the path does not need to pass
    through the root.

    The path sum of a path is the sum of the node's values in the path.

    Given the root of a binary tree, return the maximum path sum of any
    non-empty path.

    Example 1:
        Input: root = [1,2,3]
        Output: 6
        Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of
            2 + 1 + 3 = 6.

    Example 2:
        Input: root = [-10,9,20,null,null,15,7]
        Output: 42
        Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of
            15 + 20 + 7 = 42.

    Constraints:
        - The number of nodes in the tree is in the range [1, 3 * 10^4].
        - -1000 <= Node.val <= 1000

思路：
    recursive(node) 回傳「以 node 為起點、向下延伸一條腿」的最大值；負腿視為 0（不接）。
    全局答案用 self.tmpMax 維護：訪問每個 node 時用「v + 左淨腿 + 右淨腿」更新（兩條腿在 node 折返）。
    為何不對稱：回傳要讓 parent 線性接 → 只能一條腿；全局答案可在當前 node 折返 → 可用兩條腿。
    self. 維護全局狀態：明確標記「跨節點累積」，不與 return 值混淆。
複雜度：
    Time: O(n) 全部點走一遍
    Space: O(h) h = 樹高 如果是skewd tree => O(n)
"""

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


def build(values):
    """Build a binary tree from a level-order list (None for missing nodes)."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.tmpMax = -float('inf')

        def recursive(node):
            if not node:
                return 0
            
            resL = recursive(node.left)
            resR = recursive(node.right)
            v = node.val
            gainL = max(resL, 0)
            gainR = max(resR, 0)
            self.tmpMax = max(self.tmpMax, v+gainR+gainL)
            return v+max(gainR, gainL)
        recursive(root)
        return self.tmpMax


if __name__ == "__main__":
    s = Solution()

    # Case 1: simple positive — path through root
    assert s.maxPathSum(build([1, 2, 3])) == 6, "Case 1"

    # Case 2: negative root — best path is in subtree
    assert s.maxPathSum(build([-10, 9, 20, None, None, 15, 7])) == 42, "Case 2"

    # Case 3: all negative — must pick single largest node
    assert s.maxPathSum(build([-3])) == -3, "Case 3: single negative"

    # Case 4: mixed negatives — exclude harmful subtree
    assert s.maxPathSum(build([2, -1, -2])) == 2, "Case 4: skip both children"

    # Case 5: long left chain
    assert s.maxPathSum(build([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])) == 48, "Case 5"

    # Edge: single node positive
    assert s.maxPathSum(build([7])) == 7, "Edge: single positive"

    # Edge: two nodes — must pick the better one alone or both
    assert s.maxPathSum(build([-2, -1])) == -1, "Edge: two negatives, pick larger alone"

    print("All tests passed!")
