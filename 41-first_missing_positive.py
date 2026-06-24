"""
41. First Missing Positive
Solved
Hard
Topics
conpanies icon
Companies
Hint
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
"""

#time: O(n)
#space: O(1)

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)
        is_one = False
        # clean data
        for i in range(n):
            if nums[i] == 1:
                is_one = True
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        
        if not is_one:
            return 1
        
        # index 0 is for n, while the rest of the index is for other value
        for i in range(n):
            value = abs(nums[i])
            if value == n:
                nums[0] = -abs(nums[0])
            else:
                nums[value] = -abs(nums[value])

        # first positive is the smallet missing positive integer
        for i in range(1,n):
            if nums[i] > 0:
                return i

        # if index 0 is not changed to negative, n is not in nums
        if nums[0] > 0:
            return n
        
        # if all nums have negative values (all exist)
        return n + 1
        
