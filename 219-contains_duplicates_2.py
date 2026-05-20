"""
219. Contains Duplicate II
Solved
Easy
Topics
conpanies icon
Companies
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.



Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""

# time: O(n)
# space: O(n)


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        num_map = set()
        left = right = 0

        while right < len(nums):
            # if window_size > k, reduce size by increasing left
            if right - left > k:
                num_map.remove(nums[left])
                left += 1

            # check if the right exist in the num_map
            if nums[right] in num_map:
                return True
            num_map.add(nums[right])
            right += 1

        return False
