
class Solution:
    def isValid(self, i, j, n, m, grid):
        return 0 <= i < n and 0 <= j < m and grid[i][j] == '1'
    
    def numIslandsRec(self, i, j, n, m, grid):
        # Mark the cell as visited by setting it to '0'
        grid[i][j] = '0'
        
        # Define directions for all 8 neighboring cells (up, down, left, right, and diagonals)
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1), # Up, down, left, right
        ]
        
        for d in directions:
            new_i, new_j = i + d[0], j + d[1]
            if self.isValid(new_i, new_j, n, m, grid):
                self.numIslandsRec(new_i, new_j, n, m, grid)
    
    def numIslands(self, grid):
        if not grid:
            return 0
        
        n = len(grid)
        m = len(grid[0])
        ans = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    ans += 1
                    self.numIslandsRec(i, j, n, m, grid)
        
        return ans