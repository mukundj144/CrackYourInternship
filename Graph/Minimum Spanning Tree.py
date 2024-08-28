import heapq
from typing import List, Tuple

class Solution:
    
    # Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[Tuple[int, int]]]) -> int:
        # Priority queue (min-heap) to get node with minimum weight
        min_heap = [(0, 0)]  # (weight, node), starting from node 0
        key = [float('inf')] * V
        visited = [False] * V
        
        # Initializing the start node
        key[0] = 0
        
        while min_heap:
            weight, node = heapq.heappop(min_heap)
            
            if visited[node]:
                continue
            
            visited[node] = True
            
            # Exploring all adjacent nodes
            for neighbour, edge_weight in adj[node]:
                if not visited[neighbour] and edge_weight < key[neighbour]:
                    key[neighbour] = edge_weight
                    heapq.heappush(min_heap, (edge_weight, neighbour))
        
        # Calculate the total weight of the MST
        total_weight = sum(key)
        
        return total_weight
