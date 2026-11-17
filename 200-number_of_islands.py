"""
200. Number of Islands
Solved
Medium

Topics
conpanies icon
Companies
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
 
Seen this question in a real interview before?
1/6
"""

# time: O(m*n)
# space: O(m*n)
# DFS 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    num_islands += 1
        return num_islands
    def dfs(self, grid, r, c):
        if (r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != "1"):
            return
        grid[r][c] = "0"

        self.dfs(grid, r - 1, c)
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r, c - 1)
        self.dfs(grid, r, c + 1)

# time: O(m*n)
# space: O(min(m,n))
# BFS via queue

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        nr = len(grid)
        nc = len(grid[0])
        num_islands = 0

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    grid[r][c] = "0"
                    queue = deque([(r,c)])
                    while queue:
                        row, col = queue.popleft()
                        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                            nr2, nc2 = row + dr, col + dc
                            if 0 <= nr2 < nr and 0 <= nc2 < nc and grid[nr2][nc2] == "1":
                                queue.append((nr2,nc2))
                                grid[nr2][nc2] = "0"
        return num_islands


