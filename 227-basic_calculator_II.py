"""
227. Basic Calculator II
Solved
Medium
Topics
conpanies icon
Companies
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5
 

Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
"""

# time: O(n)
# space: O(n)

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        op = '+'
        num = 0
        for index, ch in enumerate(s):
            if ch.isdigit():
                num = num*10 + int(ch)
            # make sure settle the last operator when its last string
            if ch in '+-*/' or index == len(s) - 1:  
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop()*num)
                elif op == '/':
                    stack.append(int(stack.pop()/num))
                num = 0
                op = ch
        return sum(stack)

# time: O(n)
# space: O(1)

class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        last_number = 0
        op = '+'
        num = 0
        for index, ch in enumerate(s):
            if ch.isdigit():
                num = num*10 + int(ch)
            # make sure settle the last operator when its last string
            if ch in '+-*/' or index == len(s) - 1:  
                if op == '+':
                    result += last_number
                    last_number = num
                elif op == '-':
                    result += last_number
                    last_number = -num
                elif op == '*':
                    last_number *= num
                elif op == "/":
                    last_number = int(last_number/num)
                op = ch
                num = 0
        return result + last_number


