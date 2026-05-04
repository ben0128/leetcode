"""
LeetCode 207. Course Schedule
Difficulty: Medium
Tags: Graph
URL: https://leetcode.com/problems/course-schedule/

Problem:
    There are a total of numCourses courses you have to take, labeled from 0 to
    numCourses - 1. You are given an array prerequisites where
    prerequisites[i] = [a_i, b_i] indicates that you must take course b_i first
    if you want to take course a_i.

    For example, the pair [0, 1] indicates that to take course 0 you have to
    first take course 1.

    Return true if you can finish all courses. Otherwise, return false.

    Example 1:
        Input: numCourses = 2, prerequisites = [[1,0]]
        Output: true
        Explanation: There are a total of 2 courses to take.
            To take course 1 you should have finished course 0. So it is
            possible.

    Example 2:
        Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
        Output: false
        Explanation: There are a total of 2 courses to take.
            To take course 1 you should have finished course 0, and to take
            course 0 you should also have finished course 1. So it is
            impossible.

    Constraints:
        - 1 <= numCourses <= 2000
        - 0 <= prerequisites.length <= 5000
        - prerequisites[i].length == 2
        - 0 <= a_i, b_i < numCourses
        - All the pairs prerequisites[i] are unique.

    Follow up:
        If you also need to RETURN a valid order in which to take the courses
        (instead of just true/false), how would you modify your approach? (See
        LeetCode 210.)

思路：
    Kahn's 

複雜度：
    V = numCourses, E = len(prerequisites)
    Time: O(V+E)
    Space: O(V+E)
"""

from typing import List
from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        numMap = defaultdict(list)
        for e, s in prerequisites:
            indegree[e] += 1
            numMap[s].append(e)

        tmp = deque([])
        count = 0
        # init 
        for i in range(numCourses):
            if indegree[i] == 0:
                count += 1
                tmp.append(i)

        while tmp:
            popN = tmp.popleft()
            for end in numMap[popN]:
                indegree[end] -= 1
                if indegree[end] == 0:
                    count += 1
                    tmp.append(end)
        return count == numCourses

if __name__ == "__main__":
    s = Solution()

    # Case 1: simple chain, possible
    assert s.canFinish(2, [[1, 0]]) is True, "Case 1"

    # Case 2: 2-cycle, impossible
    assert s.canFinish(2, [[1, 0], [0, 1]]) is False, "Case 2"

    # Case 3: longer chain, possible
    assert s.canFinish(4, [[1, 0], [2, 1], [3, 2]]) is True, "Case 3"

    # Case 4: longer cycle (3-cycle), impossible
    assert s.canFinish(3, [[0, 1], [1, 2], [2, 0]]) is False, "Case 4"

    # Edge: no prerequisites at all
    assert s.canFinish(5, []) is True, "Edge: no prereqs"

    # Edge: self-loop, impossible
    assert s.canFinish(1, [[0, 0]]) is False, "Edge: self-loop"

    print("All tests passed!")
