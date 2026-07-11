"""
424. Longest Repeating Character Replacement
Attempted
Medium
Topics
conpanies icon
Companies
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""

#time: O(n^2)
#space: O(1)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        for i in range(len(s)):
            freq = Counter()
            for j in range(i,len(s)):
                freq[s[j]] += 1
                max_freq = max(freq.values())
                length_substring = j - i + 1
                char_to_change = length_substring - max_freq

                if char_to_change <= k:
                    ans = max(ans,length_substring)

        return ans
