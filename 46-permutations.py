"""

46. Permutations
Medium
Topics
conpanies icon
Companies
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""

# time: O(n*n!)
# space: O(n)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def backTrack(curr: str):
            if len(curr) == n:
                ans.append(curr[:])
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backTrack(curr)
                    curr.pop()
        backTrack([])
        return(ans)
