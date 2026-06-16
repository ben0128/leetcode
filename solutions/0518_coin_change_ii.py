"""
LeetCode 518. Coin Change II
Difficulty: Medium
Tags: Array
URL: https://leetcode.com/problems/coin-change-ii/

Problem:
    You are given an integer array coins representing coins of different
    denominations and an integer amount representing a total amount of money.

    Return the number of combinations that make up that amount. If that amount
    of money cannot be made up by any combination of the coins, return 0.

    You may assume that you have an infinite number of each kind of coin.

    The answer is guaranteed to fit into a signed 32-bit integer.

    Example 1:
        Input: amount = 5, coins = [1,2,5]
        Output: 4
        Explanation: the four combinations are:
            5 = 5
            5 = 2+2+1
            5 = 2+1+1+1
            5 = 1+1+1+1+1
            (note: 2+2+1 and 1+2+2 count as the SAME combination)

    Example 2:
        Input: amount = 3, coins = [2]
        Output: 0
        Explanation: the amount of 3 cannot be made up just with coins of 2.

    Example 3:
        Input: amount = 10, coins = [10]
        Output: 1

    Constraints:
        - 1 <= coins.length <= 300
        - 1 <= coins[i] <= 5000
        - All the values of coins are unique.
        - 0 <= amount <= 5000

    思路:
    DP (one-dimension dynamic programming): the DP index i means the combination of the current amount i.                                                                                                           
  The time complexity is the length of the coins multiplied by the amount, and the space complexity is O(amount).                                                                                                 
                                                                                                                                                                                                                  
  I will use a double for loop, where the outer loop is coins and the inner loop is amount
  The key reason for the double for loop is that if I loop through the coin first, it can avoid duplicated combinations.                                                                                       
                                                                                                                                                                                                                  
  If I have already looped through a coin (like a value of one) and then move on to the next coins, it ensures I won't recalculate the previous values of a coin in the next loop. I think that is the reason.    
  for example if I want have coins = [1, 2, 3]       dp[3] += dp[3-2], dp[3] += dp[3-1]    it will cause dup, like (1,2), (2,1)          
  dp[i] += dp[i-coin]                                                                                                                                                                                          
  2: dp[0] = 1   
  
    tc = O(len(coins)* amount)
    sc = O(amount)
"""


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1

        for coin in coins:
            for count in range(coin, amount+1):
                dp[count] += dp[count-coin]
        return dp[-1]


if __name__ == "__main__":
    s = Solution()

    # Example 1: 4 distinct combinations
    assert s.change(5, [1, 2, 5]) == 4, "Case 1"

    # Example 2: impossible -> 0
    assert s.change(3, [2]) == 0, "Case 2"

    # Example 3: single exact coin -> 1
    assert s.change(10, [10]) == 1, "Case 3"

    # Edge: amount = 0 -> 1 (the empty combination)
    assert s.change(0, [1, 2, 5]) == 1, "Edge: amount 0"

    # Combinations vs permutations check: 1+2 and 2+1 are the SAME -> 2 ways for amount 3
    assert s.change(3, [1, 2]) == 2, "Edge: combos not perms"
    
    assert s.change(4, [10, 12]) == 0

    print("All tests passed!")
