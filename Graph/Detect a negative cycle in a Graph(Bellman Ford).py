class Solution:
    def bellmanFord(self, n, edges, src):
        # Initialize distances with infinity, except for the source
        dist = [float('inf')] * n
        dist[src] = 0

        # Relax all edges n-1 times
        for _ in range(n - 1):
            for u, v, wt in edges:
                if dist[u] != float('inf') and dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt

        # Check for negative weight cycles
        for u, v, wt in edges:
            if dist[u] != float('inf') and dist[u] + wt < dist[v]:
                return True  # Negative weight cycle detected

        return False  # No negative weight cycle found

    def isNegativeWeightCycle(self, n, edges):
        # Check all nodes as the source for negative weight cycles
        for src in range(n):
            if self.bellmanFord(n, edges, src):
                return 1  # Negative weight cycle exists

        return 0  # No negative weight cycle found