"""
78. Subsets
Medium
Topics
conpanies icon
Companies
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""

# time: O(n*2^n)
# space: O(n*2^n)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            newSubsets = []
            for curr in ans:
                temp = curr[:]
                temp.append(num)
                newSubsets.append(temp)
            for curr in newSubsets:
                ans.append(curr)
        return ans


# time: O(n*2^n)
# space: O(n)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def backTrack(curr: str, start: int):
            ans.append(curr[:])
            for i in range(start,n):
                curr.append(nums[i])
                backTrack(curr, i + 1)
                curr.pop()
        backTrack([],0)
        return ans




