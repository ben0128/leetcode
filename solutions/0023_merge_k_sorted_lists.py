"""
LeetCode 23. Merge k Sorted Lists
Difficulty: Hard
Tags: Linked List
URL: https://leetcode.com/problems/merge-k-sorted-lists/

Problem:
    You are given an array of k linked-lists `lists`, each linked-list is
    sorted in ascending order.

    Merge all the linked-lists into one sorted linked-list and return it.

    Example 1:
        Input: lists = [[1,4,5],[1,3,4],[2,6]]
        Output: [1,1,2,3,4,4,5,6]
        Explanation: The linked-lists are:
            [
              1->4->5,
              1->3->4,
              2->6
            ]
        merging them into one sorted list:
            1->1->2->3->4->4->5->6

    Example 2:
        Input: lists = []
        Output: []

    Example 3:
        Input: lists = [[]]
        Output: []

    Constraints:
        - k == lists.length
        - 0 <= k <= 10^4
        - 0 <= lists[i].length <= 500
        - -10^4 <= lists[i][j] <= 10^4
        - lists[i] is sorted in ascending order.
        - The sum of lists[i].length will not exceed 10^4.

思路：
    我使用 min-heap 推入一個 tuple，「tuple 三個元素：value / idx（tie-break：val 相等時靠它比，否則 Python 會去比
  ▎ ListNode 而報錯） / node 本身。利用 min-heap 由小到大的特色，當我 pop 出來是所有 list 當前最前節點裡的最小。
    在 pop 出來之後，我會建立一個 dummy, pop 出來的這個點接上去，讓 dummy 指向這個點。接著繼續跑 while 迴圈，一路把所有的點接完。
複雜度：
    n = 全部點數量, k = list 數量
    Time:  O(N log k) 
    Space: O(k)
"""

from typing import List, Optional
from heapq import heappush, heappop

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = head = ListNode(None)

        minH = []
        for idx, list in enumerate(lists):
            if list:
                heappush(minH, (list.val, idx, list))
        
        while minH:
            _, i, n = heappop(minH)
            
            head.next = n
            head = head.next 
            n = n.next
            if n:
                heappush(minH, (n.val, i, n))
            
        return dummy.next


if __name__ == "__main__":
    def build(arr):
        """Build a linked list from a Python list; return its head."""
        dummy = ListNode()
        cur = dummy
        for x in arr:
            cur.next = ListNode(x)
            cur = cur.next
        return dummy.next

    def to_list(head):
        """Flatten a linked list back into a Python list."""
        out = []
        while head:
            out.append(head.val)
            head = head.next
        return out

    sol = Solution()

    # Test cases
    r1 = sol.mergeKLists([build([1, 4, 5]), build([1, 3, 4]), build([2, 6])])
    assert to_list(r1) == [1, 1, 2, 3, 4, 4, 5, 6], f"Case 1 failed: {to_list(r1)}"

    r2 = sol.mergeKLists([build([1, 2, 3]), build([4, 5, 6]), build([7, 8, 9])])
    assert to_list(r2) == [1, 2, 3, 4, 5, 6, 7, 8, 9], f"Case 2 failed: {to_list(r2)}"

    # Edge: empty array of lists
    assert to_list(sol.mergeKLists([])) == [], "Edge: no lists"

    # Edge: a single empty list
    assert to_list(sol.mergeKLists([build([])])) == [], "Edge: one empty list"

    # Edge: some lists empty, some not
    r5 = sol.mergeKLists([build([]), build([1]), build([]), build([0, 2])])
    assert to_list(r5) == [0, 1, 2], f"Edge mixed-empty failed: {to_list(r5)}"

    # Edge: single list with negatives
    r6 = sol.mergeKLists([build([-10, -1, 5])])
    assert to_list(r6) == [-10, -1, 5], f"Edge single list failed: {to_list(r6)}"

    r7 = sol.mergeKLists([build([-10, 1, 2]), build([]), build([])])
    assert to_list(r7) == [-10, 1, 2], f"Edge mixed-empty failed: {to_list(r7)}"
    
    assert to_list(sol.mergeKLists([build([1, 1]), build([1, 1]), build([1])])) == [1, 1,1, 1, 1]
    print("All tests passed!")
