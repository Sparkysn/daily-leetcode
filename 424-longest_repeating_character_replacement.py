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

#time: O(nlogn)
#space: O(1)

# binarysearch + sliding window

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lo, hi = 1, len(s)

        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if self.canMakeValidSubString(mid, s, k):
                lo = mid
            else:
                hi = mid
        
        if self.canMakeValidSubString(hi, s ,k):
            return hi
        if self.canMakeValidSubString(lo, s, k):
            return lo
        return 1
    def canMakeValidSubString(self, windowLength: int, s: str, k: int) -> bool:
        start = 0
        maxFrequency = 0
        freq = {}

        for end in range(len(s)):
            freq[s[end]] = freq.get(s[end], 0) + 1

            if end - start + 1 > windowLength:
                freq[s[start]] -= 1
                start += 1
            
            if end - start + 1 == windowLength:
                maxFrequency = max(freq.values())
                if maxFrequency + k >= windowLength:
                    return True

        return False

# time: O(mn) -> O(n)
# space: O(1)

# sliding window (slow)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = set(s)
        max_length = 0

        for char in chars:
            start = 0
            count = 0

            for end in range(len(s)):
                if s[end] == char:
                    count += 1

                while not self.isValidWindow(start, end, count, k):
                    if s[start] == char:
                        count -= 1
                    start += 1
                max_length = max(max_length, end - start + 1)
                
        return max_length

    def isValidWindow(self, start: int, end: int, count: int, k: int) -> int:
        return (end - start + 1) - count <= k


# time: O(n)
# space: O(1)

# sliding window (fast)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        freq = {}
        max_freq = 0
        longest_substring_length = 0

        for end in range(len(s)):
            freq[s[end]] = freq.get(s[end], 0) + 1

            max_freq = max(max_freq, freq[s[end]])

            is_valid = (end - start + 1) - max_freq <= k
            if not is_valid:
                freq[s[start]] -= 1
                start += 1
            
            longest_substring_length = end - start + 1
        return longest_substring_length
