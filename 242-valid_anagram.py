"""
242. Valid Anagram
Solved
Easy
Topics
conpanies icon
Companies
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

#time: O(nlogn)
#space: O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

#time: O(n)
#space: O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letter_dict = {}
        for char in s:
            if char not in letter_dict:
                letter_dict[char] = 1
            else:
                letter_dict[char] += 1
        
        for char in t:
            if char not in letter_dict or letter_dict[char] == 0:
                return False
            else:
                letter_dict[char] -= 1
        return True
            

