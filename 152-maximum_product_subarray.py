"""
152. Maximum Product Subarray
Attempted
Medium
Topics
conpanies icon
Companies
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
"""


#time: O(n^2)
#space: O(1)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = float('-inf')
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):
            product = nums[i]
            max_product = max(max_product, product)
            for j in range(i+1, len(nums)):
                product*= nums[j]
                max_product = max(max_product, product)
        return max_product if max_product != float('-inf') else 0
            



#time: O(n)
#space: O(1)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # initialise 
        max_so_far = min_so_far = result = nums[0]
        for i in range(1,len(nums)):
            curr = nums[i]
            temp_max = max(curr, max(min_so_far * curr, max_so_far * curr))
            min_so_far = min(curr, min(min_so_far * curr, max_so_far * curr))
            
            max_so_far = temp_max
            result = max(max_so_far, result)
        
        return result
