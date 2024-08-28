from typing import List

class Solution:
    
    # Function to detect cycle in a directed graph.
    def isCyclic(self, V: int, adj: List[List[int]]) -> bool:
        def dfs(v: int) -> bool:
            visited[v] = True
            dfsVisited[v] = True
            
            # Recur for all neighbors
            for neighbor in adj[v]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
                elif dfsVisited[neighbor]:
                    return True
            
            dfsVisited[v] = False
            return False
        
        visited = [False] * V
        dfsVisited = [False] * V
        
        for i in range(V):
            if not visited[i]:
                if dfs(i):
                    return True
        
        return False