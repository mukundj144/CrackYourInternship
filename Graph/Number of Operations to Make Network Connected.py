from collections import defaultdict

class Solution:
    def dfs(self, src, g, vis):
        vis[src] = 1
        for x in g[src]:
            if not vis[x]:
                self.dfs(x, g, vis)
    
    def makeConnected(self, n: int, edges: list[list[int]]) -> int:
        if len(edges) < n - 1:
            return -1
        
        # Create adjacency list
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        # Initialize visited list
        vis = [0] * n
        c = 0
        
        # Count connected components
        for i in range(n):
            if not vis[i]:
                c += 1
                self.dfs(i, g, vis)
        
        return c - 1
