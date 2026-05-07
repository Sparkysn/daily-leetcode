"""
4. Rotate image

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""

# time: O(n)
# space: O(n)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        n = len(matrix)
        tuple_value = {}

        if n == 1:
            return
        
        elif (n % 2 == 0): # even
            for i in range (0,n):
                for j in range (0,n):
                    if (i,j) not in tuple_value:
                        if (j,n-i-1) not in tuple_value:
                            tuple_value[(j,n-i-1)] = matrix[j][n-i-1]     
                        matrix[j][n-i-1] = matrix[i][j]
                    else:
                        if (j,n-i-1) not in tuple_value:
                            tuple_value[(j,n-i-1)] = matrix[j][n-i-1]
                        matrix[j][n-i-1] = tuple_value[(i,j)]
        
        else: # odd
            middle_value = n // 2
            for i in range (0,n):
                for j in range (0,n):
                    if (i == middle_value and j == middle_value):
                        continue
                    if (i,j) not in tuple_value:
                        if (j,n-i-1) not in tuple_value:
                            tuple_value[(j,n-i-1)] = matrix[j][n-i-1]     
                        matrix[j][n-i-1] = matrix[i][j]
                    else:
                        if (j,n-i-1) not in tuple_value:
                            tuple_value[(j,n-i-1)] = matrix[j][n-i-1]
                        matrix[j][n-i-1] = tuple_value[(i,j)]







        