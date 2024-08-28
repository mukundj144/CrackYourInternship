from typing import List

class Solution:
    def findPath(self, m: List[List[int]]) -> List[str]:
        def is_safe(x: int, y: int) -> bool:
            return 0 <= x < len(m) and 0 <= y < len(m[0]) and m[x][y] == 1 and not visited[x][y]
        
        def dfs(x, y, path):
            if x == len(m) - 1 and y == len(m[0]) - 1:  # Destination reached
                paths.append(path)
                return
            
            visited[x][y] = True
            
            # Move Down
            if is_safe(x + 1, y):
                dfs(x + 1, y, path + "D")
            
            # Move Left
            if is_safe(x, y - 1):
                dfs(x, y - 1, path + "L")
            
            # Move Right
            if is_safe(x, y + 1):
                dfs(x, y + 1, path + "R")
            
            # Move Up
            if is_safe(x - 1, y):
                dfs(x - 1, y, path + "U")
            
            visited[x][y] = False  # Backtrack
        
        if not m or m[0][0] == 0:
            return []  # No path if start is blocked
        
        paths = []
        visited = [[False] * len(m[0]) for _ in range(len(m))]
        dfs(0, 0, "")
        return paths
