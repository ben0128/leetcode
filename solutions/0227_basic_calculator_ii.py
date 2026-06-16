"""
LeetCode 227. Basic Calculator II
Difficulty: Medium
Tags: String, Math
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
    會先 init 三個變數：

1. result：最後的歸檔區
2. lastNum
3. num

lastNum 和 num 這兩個數字會在中間互相影響，所以要記錄他們中間的運算符號是什麼，因此還會有一個 prev_op 去記錄最後出現的運算符
　當出現加號或減號時，就直接將 last number 歸檔入 result，然後將 last number 令為 num，並且要注意正負。

而如果是出現乘除時，last number 就要吸收 num

複雜度：
    Time: O(n)
    Space: O(1)
"""


class Solution:
    def calculate(self, s: str) -> int:
        res, lastNum, num = 0, 0, 0
        prev_op = '+'
        ops = {
            '+': lambda a, b: a+b,
            '-': lambda a, b: a-b,
            '*': lambda a, b: a*b,
            '/': lambda a, b: int(a/b)
        }
        
        for c in s:
            if c == ' ':
                continue
            elif c in '0123456789':
                num = num*10 + int(c)
            else:
                if prev_op == '+':
                    res += lastNum
                    lastNum = num
                elif prev_op == '-':
                    res += lastNum
                    lastNum = -num
                elif prev_op == '*':
                    lastNum *= num
                else:
                    lastNum = int(lastNum/num)
                prev_op = c
                num = 0

        return res + ops[prev_op](lastNum,num)
                


if __name__ == "__main__":
    s = Solution()

    assert s.calculate("3+2*2") == 7, "Case 1"
    assert s.calculate(" 3/2 ") == 1, "Case 2"
    assert s.calculate(" 3+5 / 2 ") == 5, "Case 3"

    # cap-point history: trailing num must flush at end (1-1+1)
    assert s.calculate("1-1+1") == 1, "Case 4: trailing flush"

    # truncate toward zero on negative dividend: int(-6/4) == -1, NOT -6//4 == -2
    assert s.calculate("1-6/4") == 0, "Case 5: truncate toward zero"

    # edge: single number with whitespace
    assert s.calculate("   42  ") == 42, "Edge: single number"
    assert s.calculate("10-6-3") == 1, "Case 6: negative number"
    print("All tests passed!")
