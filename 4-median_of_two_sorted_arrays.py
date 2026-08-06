"""
4. Median of Two Sorted Arrays
Solved
Hard
Topics
conpanies icon
Companies
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""


# time: O(n)
# space: O(1)

# two pointer

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        total_len = m + n
        p1, p2 = 0, 0

        curr = prev = 0

        for _ in range((total_len // 2) + 1):
            prev = curr
            if p1 < m and (p2 >= n or nums1[p1] <= nums2[p2]):
                curr = nums1[p1]
                p1 += 1
            else:
                curr = nums2[p2]
                p2 += 1
        if total_len % 2 == 0:
            # even
            return (prev + curr) / 2
        return curr

# time: O(log(n+m))
# space: O(log(n+m))

# binary search 

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        na, nb = len(A), len(B)
        n = na + nb

        def solve(k, a_start, a_end, b_start, b_end):
            # if segment of the array is empty, means all index is processed, the answer lies in other array
            # take the offset of opposite array
            # note that if a_start == a_end, means still have 1 index in array
            if a_start > a_end:
                return B[k-a_start]
            if b_start > b_end:
                return A[k-b_start]
            # get middle index 
            a_index, b_index = (a_start + a_end) // 2, (b_start + b_end) // 2
            a_value, b_value = A[a_index], B[b_index]

            # if k is right of half of (A + B), remove smaller left half
            if a_index + b_index < k:
                if a_value > b_value:
                    return solve(k, a_start, a_end, b_index + 1, b_end)
                else:
                    return solve(k, a_index + 1, a_end, b_start, b_end)
            # k left of half of (A + B), remove bigger right half
            else:
                if a_value > b_value:
                    return solve(k, a_start, a_index - 1, b_start, b_end)
                else:
                    return solve(k, a_start, a_end, b_start, b_index - 1)
        # odd, take middle
        if n % 2 != 0:
            return solve(n//2,0,na-1,0,nb-1)
        # even, take avg
        else:
            return (
                solve(n // 2, 0, na - 1, 0, nb - 1)
                + solve(n // 2 - 1, 0, na - 1, 0, nb - 1)
            ) / 2




                
                

        
