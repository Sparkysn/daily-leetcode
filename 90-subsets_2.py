"""
90. Subsets II
Solved
Medium
Topics
conpanies icon
Companies
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""

# time: O(n*2^n)
# space: O(n)

# bitmasking

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()
        n = len(nums)
        ans = []
        for i in range(2**n,2**(n+1)):
            bitmask = bin(i)[3:]
            subset = []
            for j in range(n):
                if bitmask[j] == "1":
                    subset.append(nums[j])
                
            if tuple(subset) not in seen:
                seen.add(tuple(subset))
                ans.append(subset)
        return ans

# time: O(n*2^n)
# space: O(n)

# backtracking

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        def backTrack(curr: list, start: int):
            ans.append(curr[:])
            for i in range(start, n):
                if i != start and nums[i] == nums[i - 1]:
                    continue
                curr.append(nums[i])
                backTrack(curr, i + 1)
                curr.pop()
        backTrack([], 0)
        return ans
