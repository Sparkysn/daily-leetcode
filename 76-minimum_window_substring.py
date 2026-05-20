"""
76. Minimum Window Substring
Solved
Hard
Topics
conpanies icon
Companies
Hint
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.


Follow up: Could you find an algorithm that runs in O(m + n) time?
"""

# time: O(m+n)
# space: O(m+n)


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t = Counter(t)  # window needs to fufil this counter
        required = len(dict_t)  # unique chars to fulfil
        formed = 0
        window_counts = {}

        left = right = 0
        min_window_len = float("inf")
        result = ""

        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1

            # check if current char fulfil requirement
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1

            # shrink left when window is valid
            while formed == required and left <= right:
                char = s[left]
                window_len = right - left + 1
                if window_len < min_window_len:
                    min_window_len = window_len
                    result = s[left : right + 1]

                # remove left from current window
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1
                left += 1

            right += 1

        return result
