"""
5. Longest Palindromic Substring
Solved
Medium
Topics
conpanies icon
Companies
Hint
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

# time: O(n^2)
# space: O(n^2)

# dp table

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_length = 1
        ans = ""

        # initialise matrix to false, a.k.a 0
        matrix = [[0] * n for _ in range(n)]

        # singular letter is confirm a palindrome (len = 1)
        for i in range(n):
            matrix[i][i] = 1
            ans = s[i:i+1]

        # adjacent letters is a palindrome if it's the same letter (len = 2)
        for i in range(n-1):
            if s[i+1] == s[i]:
                matrix[i][i+1] = 1
                max_length = 2
                ans = s[i:i+2]

        # Bigger length of string is a palindrome if outer 2 is same, and inner string is palindrome (len > 2)
        for gap in range(2,n):
            for i in range(n-gap):
                j = i + gap
                if matrix[i+1][j-1] == 1 and s[i] == s[j]:
                    matrix[i][j] = 1
                    if j-i+1 > max_length:
                        max_length = j-i+1
                        ans = s[i:j+1]

        return ans
                
