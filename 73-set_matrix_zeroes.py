"""
73. Set Matrix Zeroes
Solved
Medium
Topics
conpanies icon
Companies
Hint
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
*m
 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

# time: O(n*m)
# space: O(n+m)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_to_zero = set()
        col_to_zero = set()

        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if val == 0:
                    row_to_zero.add(r)
                    col_to_zero.add(c)
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in row_to_zero or c in col_to_zero:
                    matrix[r][c] = 0

# time: O(n*m)
# space: O(1)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row_flag = False
        col_flag = False
        # see if row 0 and col 0 has any 0's
        for c in range(n):
            if matrix[0][c] == 0:
                row_flag = True
                break
        for r in range(m):
            if matrix[r][0] == 0:
                col_flag = True
                break
        # use row 0 and col 0 as markers
        for r in range(1,m):
            for c in range(1,n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        # zero out based on markers
        for r in range(1,m):
            for c in range(1,n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        # handle row 0 and col 0 based on flags
        if row_flag:
            for c in range(n):
                matrix[0][c] = 0
        if col_flag:
            for r in range(m):
                matrix[r][0] = 0

                    
                
        
                
        


