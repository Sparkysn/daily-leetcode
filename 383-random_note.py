"""
383. Ransom Note
Solved
Easy
Topics
conpanies icon
Companies
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""

# time: O(n)
# space: O(n)

# remove char one by one

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for c in ransomNote:
            if c not in magazine:
                return False
            location = magazine.index(c)
            magazine = magazine[:location] + magazine[location+1:]
        return True

# time: O(n)
# space: O(1)

# hashmap

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counter = Counter(magazine)
        for char in ransomNote:
            if char not in magazine_counter or magazine_counter[char] <= 0:
                return False
            else:
                magazine_counter[char] -= 1
        return True

# time: O(nlogn)
# space: O(n)

# sort and stack

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        ransomNote = sorted(ransomNote,reverse=True)
        magazine = sorted(magazine,reverse=True)
        while ransomNote and magazine:
            if ransomNote[-1] == magazine[-1]:
                ransomNote.pop()
                magazine.pop()
            elif magazine[-1] < ransomNote[-1]:
                magazine.pop()
            else:
                return False
        if ransomNote:
            return False
        return True
