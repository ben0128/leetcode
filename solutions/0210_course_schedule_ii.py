"""
LeetCode 210. Course Schedule II
Difficulty: Medium
Tags: Graph
URL: https://leetcode.com/problems/course-schedule-ii/

Problem:
    There are a total of numCourses courses you have to take, labeled from
    0 to numCourses - 1. You are given an array prerequisites where
    prerequisites[i] = [ai, bi] indicates that you must take course bi
    first if you want to take course ai.

    For example, the pair [0, 1] indicates that to take course 0 you have
    to first take course 1.

    Return the ordering of courses you should take to finish all courses.
    If there are many valid answers, return any of them. If it is
    impossible to finish all courses, return an empty array.

    Example 1:
        Input: numCourses = 2, prerequisites = [[1, 0]]
        Output: [0, 1]
        Explanation: There are a total of 2 courses to take. To take
        course 1 you should have finished course 0. So the correct order
        is [0, 1].

    Example 2:
        Input: numCourses = 4, prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        Output: [0, 2, 1, 3]
        Explanation: There are a total of 4 courses to take. To take
        course 3 you should have finished both courses 1 and 2. Both
        courses 1 and 2 should be taken after you finished course 0. So
        one correct course order is [0, 1, 2, 3]. Another correct ordering
        is [0, 2, 1, 3].

    Example 3:
        Input: numCourses = 1, prerequisites = []
        Output: [0]

    Constraints:
        - 1 <= numCourses <= 2000
        - 0 <= prerequisites.length <= numCourses * (numCourses - 1)
        - prerequisites[i].length == 2
        - 0 <= ai, bi < numCourses
        - ai != bi
        - All the pairs [ai, bi] are distinct.

思路：
    TODO（Plan #7 4-段強制：演算法骨架 / 資料結構+理由 / Invariant / 複雜度）
    第一段先 init 一個 visit 陣列，目的是為了要在後續知道哪些點已經走過、哪些點正在走、哪些點還沒走過，分清楚這三種狀態。

接著建立一個 graph，把題目給的 prerequisites 改成 graph 版本。建立完 graph 之後，接下來就跑 DFS 把所有的點走一遍：

1. 如果跑的過程中發現已經有灰色點了，代表這條路徑上面有 circle，就直接 early return 答案。
2. 如果沒有的話，就在查找完整條路徑之後，反向把點放進答案中，最後把這個點標成黑色。
3. 最後把這個 answer 再反向一次，並且要檢查 answer 裡面的課程長度，確認是否剛好符合課程數。
  ▎ 🟡灰 = 正在走 狀態；⚫黑 = 走過 狀態。碰到灰 → 環，因為 正在走這條路。
    強制用 DFS（不准用 Kahn's BFS——#207 已寫過）

複雜度：
    n = 節點數量, m = 邊數量
    Time: O(n+m)
    Space: O(n+m)
"""

from typing import List
from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = [0 for _ in range(numCourses)]
        
        nodeGraph = defaultdict(list)
        for end, start in prerequisites:
            nodeGraph[start].append(end)

        self.ans = []
        # 先檢查該點是否為灰色(-1), 如果是代表當前路徑有circle, return false, 遇到黑色(1) 就直接skip 代表走過了
        def dfs(entry):
            status = visited[entry]
            if status == -1:
                return False
            elif status == 1:
                return True
            else:
                visited[entry] = -1
                for nxtNode in nodeGraph[entry]:
                    if not dfs(nxtNode):
                        return False
            
            self.ans.append(entry)
            visited[entry] = 1
            return True
        for node in range(numCourses):
            if not dfs(node):
                return []
        return self.ans[::-1]



if __name__ == "__main__":
    sol = Solution()
    # Helper to verify any valid topological order
    def is_valid_order(order, num, prereqs):
        if len(order) != num:
            return False
        pos = {c: i for i, c in enumerate(order)}
        if len(pos) != num:
            return False
        for a, b in prereqs:
            if pos[b] >= pos[a]:
                return False
        return True

    # Test cases
    res1 = sol.findOrder(2, [[1, 0]])
    assert is_valid_order(res1, 2, [[1, 0]]), f"Case 1 failed: {res1}"

    res2 = sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    assert is_valid_order(res2, 4, [[1, 0], [2, 0], [3, 1], [3, 2]]), f"Case 2 failed: {res2}"

    res3 = sol.findOrder(1, [])
    assert is_valid_order(res3, 1, []), f"Case 3 failed: {res3}"

    # Edge: cycle → return []
    assert sol.findOrder(2, [[1, 0], [0, 1]]) == [], "Cycle case"

    # Regression: cycle in a component unreachable from any in-degree-0 node
    # (caught a real bug: starting DFS only from in-degree-0 nodes missed this)
    assert sol.findOrder(3, [[1, 2], [2, 1]]) == [], "Disconnected cycle"

    # Edge: no prereqs, multiple courses
    res5 = sol.findOrder(3, [])
    assert is_valid_order(res5, 3, []), f"No prereqs failed: {res5}"

    # Edge: longer chain
    res6 = sol.findOrder(6, [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4]])
    assert is_valid_order(res6, 6, [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4]]), f"Chain failed: {res6}"

    print("All tests passed!")
