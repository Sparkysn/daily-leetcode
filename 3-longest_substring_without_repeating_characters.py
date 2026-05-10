"""
3. Longest Substring Without Repeating Characters
Solved
Medium
Topics
conpanies icon
Companies
Hint
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

# time: O(2n)
# space: O(n)

from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        chars = Counter()
        left = 0
        right = 0
        res = 0

        while (right < len(s)):
            r = s[right]
            chars[r] += 1

            while (chars[r] > 1):
                l = s[left]
                chars[l] -= 1
                left += 1

            res = max(res, right - left + 1)
            right += 1

        return res
    
# time: O(n)
# space: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        left = 0
        right = 0 
        pos_map = {}

        while (right < len(s)):
            if (s[right] in pos_map):
                left = max(left, pos_map[s[right]] + 1)
            pos_map[s[right]] = right
            ans = max(right - left + 1, ans)
            right += 1

        return ans
            