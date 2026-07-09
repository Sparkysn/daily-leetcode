"""
239. Sliding Window Maximum
Attempted
Hard
Topics
conpanies icon
Companies
Hint
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""

#time: O(n^2)
#space: O(n)

# brute force

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_array = []
        for i in range(len(nums)-k+1):
            temp_max_number = float('-inf')
            for j in range(i,i+k):
                temp_max_number = max(temp_max_number,nums[j])
            max_array.append(temp_max_number)
        return max_array

#time: O(n)
#space: O(n)

# deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        ans_array = []
        
        for i in range(len(nums)):
            # remove indices outside of window
            while window and window[0] <= i - k:
                window.popleft()
            # remove indices that are lesser than current nums[i], as they will never be max
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            
            window.append(i)

            # add max into answer if window is formed
            if i >= k - 1:
                ans_array.append(nums[window[0]])
        return ans_array


#time: O(n)
#space: O(n)

# dynamic programming

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        left = [0]* n
        right = [0]* n
        ans_array = [0]* (n - k + 1)

        for i in range(n):
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(nums[i],left[i-1])
        right[n-1] = nums[n-1]
        for i in range(n-2,-1,-1):
            if (i+1) % k == 0:
                right[i] = nums[i]
            else:
                right[i] = max(nums[i],right[i+1])
        
        for i in range(n-k+1):
            ans_array[i] = max(right[i],left[i+k-1])

        return ans_array



