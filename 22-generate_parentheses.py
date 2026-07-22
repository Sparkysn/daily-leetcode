"""
22. Generate Parentheses
Solved
Medium
Topics
conpanies icon
Companies
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
"""

# time: O(2^2n * n)
# space: O(2^2n * n)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        queue = deque([""])
        answer = []
        while queue:
            curr_string = queue.popleft()
            if len(curr_string) == 2*n:
                if self.isValid(curr_string):
                    answer.append(curr_string)
                continue
            queue.append(curr_string + "(")
            queue.append(curr_string + ")")
        return answer
    
    def isValid(self, s: str) -> bool:
        left_count = 0
        for char in s:
            if char == "(":
                left_count += 1
            elif char == ")":
                if left_count <= 0:
                    return False
                left_count -= 1
        return left_count == 0
    
