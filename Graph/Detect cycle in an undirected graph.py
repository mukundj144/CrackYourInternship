from typing import List

class Solution:
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        def dfs(v, visited, parent):
            visited[v] = True
            
            for neighbor in adj[v]:
                if not visited[neighbor]:
                    if dfs(neighbor, visited, v):
                        return True
                elif neighbor != parent:
                    return True
            return False
        
        visited = [False] * V
        
        for i in range(V):
            if not visited[i]:
                if dfs(i, visited, -1):
                    return True
        return False

