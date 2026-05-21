"""
LeetCode 863. All Nodes Distance K in Binary Tree
Difficulty: Medium
Tags: Tree
URL: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

Problem:
    Given the root of a binary tree, the value of a target node target, and
    an integer k, return an array of the values of all nodes that have a
    distance k from the target node.

    You can return the answer in any order.

    Example 1:
        Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
        Output: [7,4,1]
        Explanation:
            The nodes that are a distance 2 from the target node (with value 5)
            have values 7, 4, and 1.

                       3
                      / \
                     5   1
                    / \ / \
                   6  2 0  8
                     / \
                    7   4

            From node 5, distance-2 nodes are:
              - 7 (down: 5 -> 2 -> 7)
              - 4 (down: 5 -> 2 -> 4)
              - 1 (up then down: 5 -> 3 -> 1)

    Example 2:
        Input: root = [1], target = 1, k = 3
        Output: []

    Constraints:
        - The number of nodes in the tree is in the range [1, 500].
        - 0 <= Node.val <= 500
        - All the values Node.val are unique.
        - target is the value of one of the nodes in the tree.
        - 0 <= k <= 1000

思路：
    1. Pass 1（DFS 建 parent map）
    2. Pass 2（BFS from target，每 node 3 個鄰居）
    3. visited set 防回頭
    4. 走 k 層後 queue 內容就是答案

複雜度：
    Time: O(tree node 數量)
    Space: O(tree node 數量)
"""

from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    """Build a binary tree from a LeetCode level-order list (None = missing)."""
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


def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


class Solution:
    def distanceK(self, root: Optional[TreeNode], target: TreeNode, k: int) -> List[int]:
        route = {root: None}
        
        def preorder(node):
            l, r = node.left, node.right
            if l:
                route[l] = node
                preorder(l)
            if r:
                route[r] = node
                preorder(r)
            return
        
        preorder(root)
        
        tmp = deque([target])
        visited = set([target])
        while k > 0 and tmp:
            k -= 1
            n = len(tmp)
            for _ in range(n):
                popEl = tmp.popleft()
                
                l, r, u = popEl.left, popEl.right, route[popEl]
                    
                if l and l not in visited:
                    visited.add(l)
                    tmp.append(l)
                if r and r not in visited:
                    visited.add(r)
                    tmp.append(r)
                if u and u not in visited:
                    visited.add(u)
                    tmp.append(u)
        return [el.val for el in tmp]


    
if __name__ == "__main__":
    s = Solution()

    # Case 1: LeetCode example — target = 5, k = 2 → [7, 4, 1]
    root1 = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    target1 = find_node(root1, 5)
    assert sorted(s.distanceK(root1, target1, 2)) == [1, 4, 7], "Case 1: standard example"

    # Case 2: single node, k = 3 → []
    root2 = build_tree([1])
    target2 = find_node(root2, 1)
    assert s.distanceK(root2, target2, 3) == [], "Case 2: single node, k too large"

    # Case 3: k = 0 → target itself
    root3 = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    target3 = find_node(root3, 5)
    assert s.distanceK(root3, target3, 0) == [5], "Case 3: k = 0 returns target"

    # Case 4: target at root, k = 1 → direct children
    root4 = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    target4 = find_node(root4, 3)
    assert sorted(s.distanceK(root4, target4, 1)) == [1, 5], "Case 4: target at root, k=1"

    # Case 5: target is a leaf — only path is upward
    root5 = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    target5 = find_node(root5, 7)
    assert sorted(s.distanceK(root5, target5, 2)) == [4, 5], "Case 5: leaf target, upward path"
    # 7 -> 2 (dist 1) -> 4 (dist 2) and 7 -> 2 -> 5 (dist 2). Distance 2 from leaf 7: {4, 5}.

    # Edge: k larger than any distance
    root6 = build_tree([1, 2])
    target6 = find_node(root6, 1)
    assert s.distanceK(root6, target6, 5) == [], "Edge: k larger than tree diameter"

    print("All tests passed!")
