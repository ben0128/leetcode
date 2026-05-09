"""
LeetCode 322. Coin Change
Difficulty: Medium
Tags: Array
URL: https://leetcode.com/problems/coin-change/

Problem:
    You are given an integer array coins representing coins of different
    denominations and an integer amount representing a total amount of money.

    Return the fewest number of coins that you need to make up that amount.
    If that amount of money cannot be made up by any combination of the coins,
    return -1.

    You may assume that you have an infinite number of each kind of coin.

    Example 1:
        Input: coins = [1,2,5], amount = 11
        Output: 3
        Explanation: 11 = 5 + 5 + 1

    Example 2:
        Input: coins = [2], amount = 3
        Output: -1

    Example 3:
        Input: coins = [1], amount = 0
        Output: 0

    Constraints:
        - 1 <= coins.length <= 12
        - 1 <= coins[i] <= 2^31 - 1
        - 0 <= amount <= 10^4

思路：
    dp[i] = fewest number of coins compose current amount i , dp[i] = min(dp[i-coin] + 1, dp[i])
    dp[0] = 0 because example 3 show output = 0
    the other cell I init them float('inf), because I can use min() to find result, 
    dp[i-coin] + 1 => I need to plus one because I add one more coin on previous result


複雜度：
    Time: O(coins*amount)
    Space: O(amount)
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0

        for coin in coins:
            for currAmount in range(coin, amount+1):
                # currAmount = index in dp
                dp[currAmount] = min(dp[currAmount-coin]+1, dp[currAmount])
        
        return dp[-1] if dp[-1] < float('inf') else -1


if __name__ == "__main__":
    s = Solution()
    # Test cases
    assert s.coinChange([1, 2, 5], 11) == 3, "Case 1"
    assert s.coinChange([2], 3) == -1, "Case 2: impossible"
    assert s.coinChange([1, 2, 5], 100) == 20, "Case 3: larger amount"
    # Edge cases
    assert s.coinChange([1], 0) == 0, "Edge: amount = 0"
    assert s.coinChange([186, 419, 83, 408], 6249) == 20, "Edge: tricky greedy fails"
    print("All tests passed!")
