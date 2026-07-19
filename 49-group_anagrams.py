"""
49. Group Anagrams
Solved
Medium
Topics
conpanies icon
Companies
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

# time: O(nlogn)
# space: O(n)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for string in strs:
            sort_string = "".join(sorted(string))
            groups[sort_string].append(string)
        output = list(groups.values())
        return output

# time: O(n)
# space: O(n)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for string in strs:
            # convert string into tuple count of alphaberts
            count = [0]* 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            groups[tuple(count)].append(string)
        return list(groups.values())
        
        
          
            
        


          
            
        


