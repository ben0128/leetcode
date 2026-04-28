"""
LeetCode 227. Basic Calculator II
Difficulty: Medium
Tags: Math, String, Stack
URL: https://leetcode.com/problems/basic-calculator-ii/

Problem:
    Given a string s which represents an expression, evaluate this expression
    and return its value.

    The integer division should truncate toward zero.

    You may assume that the given expression is always valid. All intermediate
    results will be in the range of [-2^31, 2^31 - 1].

    Note: You are not allowed to use any built-in function which evaluates
    strings as mathematical expressions, such as eval().

    Example 1:
        Input:  s = "3+2*2"
        Output: 7

    Example 2:
        Input:  s = " 3/2 "
        Output: 1

    Example 3:
        Input:  s = " 3+5 / 2 "
        Output: 5

    Constraints:
        - 1 <= s.length <= 3 * 10^5
        - s consists of integers and operators ('+', '-', '*', '/') separated
          by some number of spaces.
        - s represents a valid expression.
        - All the integers in the expression are non-negative integers in the
          range [0, 2^31 - 1].
        - The answer is guaranteed to fit in a 32-bit integer.

思路：
    res = 已經不會變的總和就放入這邊
    lastNum = 有可能會因為後續數字所改變的部分
    prev_op = 前一個op,並非當前的op

裡面值得注意的是：
1. 減號：需要先補一個負號給它（轉成負數），方便後續統一用加法做處理。
2. 除號：則是要注意運算規則 -3 // 2 = -2（floor，往 -∞）                                                                                                                                
  - int(-3 / 2) = -1（truncate toward zero） 。

複雜度：
    Time: O(n) n = len(s)
    Space: O(1)
"""

class Solution:
    def calculate(self, s: str) -> int:
        lastNum = 0
        res = 0
        prev_op = '+'
        num = 0
        def applyOperators(value):
            nonlocal lastNum, res
            if prev_op == '+':
                res += lastNum
                lastNum = value
            elif prev_op == '-':
                res += lastNum
                lastNum = -value
            elif prev_op == '*':
                lastNum *= value
            elif prev_op == '/':
                lastNum = int(lastNum / value)

        for c in s:
            if c in '+-*/':
                applyOperators(num)
                num = 0
                prev_op = c
            elif c.isdigit():
                num = num * 10 + int(c)
        applyOperators(num)
        return res+lastNum


if __name__ == "__main__":
    s = Solution()

    # Example 1: mix of + and *
    assert s.calculate("3+2*2") == 7, "Case 1"

    # Example 2: division truncates toward zero
    assert s.calculate(" 3/2 ") == 1, "Case 2"

    # Example 3: order of operations with division
    assert s.calculate(" 3+5 / 2 ") == 5, "Case 3"

    # Edge: single number with whitespace
    assert s.calculate("   42  ") == 42, "Edge: single number"

    # Edge: multiple precedence interactions
    assert s.calculate("14-3/2") == 13, "Edge: 14 - (3/2) = 14 - 1 = 13"

    # Edge: chained */ with division truncation toward zero
    assert s.calculate("1*2-3/4+5*6-7*8+9/10") == -24, "Edge: chained ops"

    assert s.calculate("1-1+1") == 1, "Case 7"
    print("All tests passed!")
