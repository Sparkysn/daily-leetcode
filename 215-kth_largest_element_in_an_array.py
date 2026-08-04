"""
215. Kth Largest Element in an Array
Solved
Medium
Topics
conpanies icon
Companies
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""

# time: O(nlogn)
# space: O(n)

# heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

# time: O(n)
# space: O(n)

# quickselect

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []

            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)

            if k <= len(left):
                return quickSelect(left, k)
            if len(left) + len(mid) < k:
                return quickSelect(right, k - len(left) - len(mid))
            return pivot

        return quickSelect(nums, k)

