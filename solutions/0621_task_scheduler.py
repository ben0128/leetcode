"""
LeetCode 621. Task Scheduler
Difficulty: Medium
Tags: Array
URL: https://leetcode.com/problems/task-scheduler/

Problem:
    You are given an array of CPU tasks, each represented by an uppercase letter
    A to Z, where different letters represent different task types. Each task takes
    one unit of time to run. For each unit of time, the CPU can complete one task
    or stay idle.

    There is a constraint: between two tasks of the SAME type, there must be at
    least n units of time (the cooldown). That is, after running a task, the CPU
    cannot run another task of the same type until at least n other time units
    have passed.

    Return the minimum number of time units the CPU needs to finish all the tasks.

    Example 1:
        Input: tasks = ["A","A","A","B","B","B"], n = 2
        Output: 8
        Explanation: A -> B -> idle -> A -> B -> idle -> A -> B
                     There must be 2 units between two A's (and two B's).

    Example 2:
        Input: tasks = ["A","C","A","B","D","B"], n = 1
        Output: 6
        Explanation: A -> C -> B -> D -> A -> B  (no idle needed)

    Example 3:
        Input: tasks = ["A","A","A","B","B","B"], n = 3
        Output: 10
        Explanation: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B

    Constraints:
        - 1 <= tasks.length <= 10^4
        - tasks[i] is an uppercase English letter.
        - 0 <= n <= 100

思路：
    (fmax-1) * n  = 能塞的空格    (fmax-1) * n + fmax + 與fmax並列相同次數的字母數
      公式之所以會長那樣，是因為用最常出現的那些數字當作骨架，找出有幾個空格可以去塞。                                                                                                        
  最頻繁的任務是瓶頸。它出現 fmax 次，彼此間又被迫間隔 n，所以光是它就鎖死了一個長度下限 (fmax-1)*(n+1)+c——這是任何排法都逃不掉的。公式算的就是這個下限，而 
  ▎ greedy（每輪優先排最頻繁的可用任務）剛好能達到這個下限，不浪費任何一格。所以「下限 = 可達」⟹ 它就是最優解。                                                                                                                                 
  至於為什麼是並列？是因為最後有可能這些並列的元素可以排在最尾巴，會溢出來，所以要加 C 個。 當不需要 IDL 的時候，就直接抓全長就好，所以是要考慮全部的長度                                 
  如果面試官的 follow-up 要回傳實際序列的話，就要用我 comment 的那個方法      

複雜度：
    Time: O(len(tasks))
    Space: O(1)
"""

from collections import deque, Counter
from heapq import heapify, heappush, heappop

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        li = list(Counter(tasks).values())
        fmax = max(li)
        c = li.count(fmax)
        return max(len(tasks), (fmax-1)*(n+1) + c)
        # maxH = [(-c, l) for l, c in Counter(tasks).items()] # 只放有效的元素(-freq, letter)
        # heapify(maxH)
        # q = deque([]) # (effectIdx, -freq, letter)
        # i = 0
        
        # while maxH or q:
        #     while q and q[0][0] == i:
        #         _, nfreq, char = q.popleft()
        #         heappush(maxH, (nfreq, char))

        #     if maxH:
        #         nfreq, char = heappop(maxH)

        #         nfreq += 1
        #         if nfreq != 0:
        #             q.append((i + n + 1, nfreq, char))
            
        #     i += 1
        # return i


if __name__ == "__main__":
    s = Solution()

    # Case 1: cooldown forces idles -> 8
    assert s.leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8, "Case 1"

    # Case 2: enough variety, no idle -> 6
    assert s.leastInterval(["A", "C", "A", "B", "D", "B"], 1) == 6, "Case 2"

    # Case 3: larger cooldown -> 10
    assert s.leastInterval(["A", "A", "A", "B", "B", "B"], 3) == 10, "Case 3"

    # Edge: n = 0 means no cooldown -> just run them all
    assert s.leastInterval(["A", "A", "A", "B", "B", "B"], 0) == 6, "Edge: n=0"

    # Edge: single task type, no cooldown
    assert s.leastInterval(["A"], 2) == 1, "Edge: single"

    print("All tests passed!")
