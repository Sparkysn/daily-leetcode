"""
647. Palindromic Substrings
Solved
Medium
Topics
conpanies icon
Companies
Hint
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
"""
#time: O(n^2)
#space: O(n^2)


class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        ans = 0
        dp = [[False]*length for _ in range(length)]
        for i in range(length):
            dp[i][i] = True
            ans += 1

        for i in range(length-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans += 1
        
        for j in range(2,length):
            for i in range(length-2):
                if dp[i+1][j-1] == True:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        ans += 1
        
        return ans







