"""
74. Search a 2D Matrix
Solved
Medium
Topics
conpanies icon
Companies
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""

# time: O(logn)
# space: O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # lets find target's row first
        n = len(matrix)
        start = 0
        end = n - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                end = mid
            else:
                start = mid
        if matrix[end][0] <= target:
            row = end
        elif matrix[start][0] <= target:
            row = start
        else:
            return False
        
        # search the col
        lo = 0
        hi = len(matrix[row]) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False

    
