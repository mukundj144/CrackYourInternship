from collections import deque

class Solution:
    def orangesRotting(self, grid):
        if not grid:
            return -1
        
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_oranges = 0
        
        # Initialize the queue with all rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        
        # If there are no fresh oranges, return 0
        if fresh_oranges == 0:
            return 0
        
        # Directions array for moving in the 4 possible directions (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        time = 0
        
        # BFS traversal
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2  # Rot this orange
                        queue.append((nx, ny))
                        fresh_oranges -= 1
            
            time += 1
        
        # Subtract 1 because the last increment of time occurs after processing the last layer
        return time - 1 if fresh_oranges == 0 else -1
       