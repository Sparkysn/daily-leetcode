"""
34. Find First and Last Position of Element in Sorted Array
Solved
Medium
Topics
conpanies icon
Companies
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""

#time: O(logn)
#space: O(1)

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]
        left = 0
        right = n - 1

        ans_left = self.findLeft(nums,target,left,right)
        ans_right = self.findRight(nums,target,left,right)

        if ans_left == -1 :
            return [-1, -1]
        
        return [ans_left, ans_right]
        
    def findLeft(self, nums: List[int], target: int, l: int, r: int) -> int:
        leftmost = -1
        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] == target:
                leftmost = mid
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return leftmost
    
    def findRight(self, nums: List[int], target: int, l: int, r: int) -> int:
        rightmost = -1
        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] == target:
                rightmost = mid
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return rightmost

        
