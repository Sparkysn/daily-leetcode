"""
658. Find K Closest Elements
Solved
Medium
Topics
conpanies icon
Companies
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3

Output: [1,2,3,4]

Example 2:

Input: arr = [1,1,2,3,4,5], k = 4, x = -1

Output: [1,1,2,3]

 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
"""

#time: O(nlogn)
#space: O(n)

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        new_arr = sorted(arr, key=lambda num: abs(num-x))

        k_closest = new_arr[:k]
        return sorted(k_closest)

#time: O(logn)
#space: O(n)

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        left = 0
        right = n - k

        while left < right:
            mid = left + (right - left) // 2
            # check difference from mid betweem start of window and end of window
            if (x - arr[mid] < arr[mid + k] - x):
                right = mid
            elif (x - arr[mid] > arr[mid + k] - x):
                left = mid + 1
            else:
                # take left side because qns prefer a < b
                right = mid
        return arr[left:left+k]
