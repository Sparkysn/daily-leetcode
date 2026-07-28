"""
378. Kth Smallest Element in a Sorted Matrix
Solved
Medium
Topics
conpanies icon
Companies
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

 

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2
 

Follow up:

Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.
"""

# time: O(nlogn)
# space: O(n)

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        N = len(matrix)
        min_heap = []

        # initalise values in heap, value, row and column

        for row in range(min(k,N)):
            min_heap.append((matrix[row][0], row, 0))
        heapify(min_heap)

        while k:
            # extract min from heap
            value, row, column = heappop(min_heap)
            # if there is still values in that row, add it in heap
            if column + 1 < N:
                heappush(min_heap, (matrix[row][column+1], row, column+1))
            k -= 1
        return value
                    

                
                
