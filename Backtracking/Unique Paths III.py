from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # Initialize variables
        zero = 0
        sx = sy = 0
        
        # Find the number of empty squares (zero) and the starting position (sx, sy)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    zero += 1
                elif grid[r][c] == 1:
                    sx, sy = r, c
        
        # Perform DFS to count unique paths
        return self.dfs(grid, sx, sy, zero)
    
    def dfs(self, grid: List[List[int]], x: int, y: int, zero: int) -> int:
        # Check for boundaries and obstacles
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == -1:
            return 0
        
        # Check if the ending square is reached
        if grid[x][y] == 2:
            return 1 if zero == -1 else 0
        
        # Mark the current square as visited
        grid[x][y] = -1
        zero -= 1
        
        # Explore all 4 directions
        total_paths = (self.dfs(grid, x + 1, y, zero) +
                       self.dfs(grid, x, y + 1, zero) +
                       self.dfs(grid, x - 1, y, zero) +
                       self.dfs(grid, x, y - 1, zero))
        
        # Backtrack
        grid[x][y] = 0
        zero += 1
        
        return total_paths
