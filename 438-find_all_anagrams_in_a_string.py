"""
438. Find All Anagrams in a String
Solved
Medium
Topics
conpanies icon
Companies
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""

# time: O(n)
# space: O(1)

# hashmap matching (slower)

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter_p = Counter(p)
        length_p = len(p)
        counter_s = {}

        start = 0
        ans = []
        for end in range(len(s)):
            counter_s[s[end]] = counter_s.get(s[end], 0) + 1
            if end - start + 1 > length_p:
                counter_s[s[start]] -= 1
                if counter_s[s[start]] == 0:
                    del counter_s[s[start]]
                start += 1
            # valid window length below
            if counter_p == counter_s:
                ans.append(start)
        return ans

# time: O(n)
# space: O(1)

# array matching (faster)

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        array_s = [0] * 26
        array_p = [0] * 26
        ans = []
        start = 0

        for char in p:
            array_p[ord(char) - ord('a')] += 1
        
        for end in range(len(s)):
            array_s[ord(s[end]) - ord('a')] += 1
            if end - start + 1 > len(p):
                array_s[ord(s[start]) - ord('a')] -= 1
                start += 1
            # window below is valid
            if array_s == array_p:
                ans.append(start)
        return ans
            
        
