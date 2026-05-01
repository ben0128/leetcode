"""
LeetCode 1235. Maximum Profit in Job Scheduling
Difficulty: Hard
Tags: Array, Binary Search, Dynamic Programming, Sorting
URL: https://leetcode.com/problems/maximum-profit-in-job-scheduling/

Problem:
    We have n jobs, where every job is scheduled to be done from startTime[i] to
    endTime[i], obtaining a profit of profit[i].

    You're given the startTime, endTime and profit arrays, return the maximum
    profit you can take such that there are no two jobs in the subset with
    overlapping time range.

    If you choose a job that ends at time X you will be able to start another
    job that starts at time X.

    Example 1:
        Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
        Output: 120
        Explanation:
            The subset chosen is the 1st and 4th job.
            Time range [1-3] + [3-6], total profit = 50 + 70 = 120.

    Example 2:
        Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
        Output: 150
        Explanation:
            The subset chosen is the 1st, 4th and 5th job.
            Profit obtained 150 = 20 + 70 + 60.

    Example 3:
        Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
        Output: 6
        Explanation: Pick only job 2 (profit 6); jobs 1, 2, 3 all overlap.

    Constraints:
        - 1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
        - 1 <= startTime[i] < endTime[i] <= 10^9
        - 1 <= profit[i] <= 10^4

思路：
    step 1: sorted by endTime
    step 2: find prev valid jobIdx, avoid overlap
    step 3: memo the process by dp

複雜度：
    n = the numbers of jobs
    Time: O(n*log(n))
    Space: O(n)
"""

from typing import List
from bisect import bisect_right

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        endTimes = [job[0] for job in jobs]
        n = len(startTime)
        # dp[i] , i = job index + 1
        dp = [0] * (n+1)

        # i = job index
        for i, [e, s, p] in enumerate(jobs):
            dpIdx = i+1
            prevDpIdx = bisect_right(endTimes, s)
            tmpMaxProfit = dp[prevDpIdx]+p
            dp[dpIdx] = max(tmpMaxProfit, dp[dpIdx-1])

        return dp[-1]

if __name__ == "__main__":
    s = Solution()

    # Case 1: pick jobs 1 and 4 → 50 + 70 = 120
    assert s.jobScheduling(
        [1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]
    ) == 120, "Case 1"

    # Case 2: pick jobs 1, 4, 5 → 20 + 70 + 60 = 150
    assert s.jobScheduling(
        [1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]
    ) == 150, "Case 2"

    # Case 3: all overlap, pick the most profitable
    assert s.jobScheduling(
        [1, 1, 1], [2, 3, 4], [5, 6, 4]
    ) == 6, "Case 3 all overlap"

    # Case 4: no overlap, take everything
    assert s.jobScheduling(
        [1, 3, 5], [2, 4, 6], [10, 20, 30]
    ) == 60, "Case 4 no overlap"

    # Edge: single job
    assert s.jobScheduling([1], [2], [50]) == 50, "Edge: single job"

    print("All tests passed!")
