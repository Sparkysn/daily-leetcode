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

# time: O(n^3)
# space: O(1)

# brute force with optimization, decrease from big window

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        for length in range(n,0,-1):
            for start in range(n - length + 1):
                if self.checkPalindrome(start, start + length, s):
                    return s[start:start+length]
    

    def checkPalindrome(self, i: int, j: int, s: str) -> bool:
        left = i
        right = j - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True

# time: O(n^2)
# space: O(1)

# expand from center

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = [0, 0]

        for i in range(len(s)):
            odd_length = self.expand(i,i,s)
            if odd_length > ans[1] - ans[0] + 1:
                dist = odd_length // 2
                ans = [i-dist,i+dist]

            even_length = self.expand(i,i+1,s)
            if even_length > ans[1] - ans[0] + 1:
                dist = (even_length // 2) - 1
                ans = [i-dist,i+dist+1]
        return s[ans[0]:ans[1]+1]
    
    def expand(self, i: int, j: int, s: str) -> int:
        left = i
        right = j

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # left and right was expanded by 2
        return right - left + 1 -2

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
                
