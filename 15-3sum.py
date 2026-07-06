"""
15. 3Sum
Solved
Medium
Topics
conpanies icon
Companies
Hint
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

#time: O(n^2)
#space: O(n)

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.findThreeSum(nums,i,ans)

        return ans


    def findThreeSum(self, nums: list[int], i: int, ans: list[list[int]]):
        # complement + nums[i] + nums[j] = 0
        seen = set()
        j = i + 1
        while j < len(nums):
            complement = -nums[i] -nums[j]
            if complement in seen:
                ans.append([nums[i],nums[j],complement])
                while j + 1 < len(nums) and nums[j] == nums[j+1]:
                    j += 1
            seen.add(nums[j])
            j += 1


        
