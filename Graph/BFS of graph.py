from typing import List
from collections import deque

class Solution:
    # Function to return Breadth First Traversal of a given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # Initialize a list to keep track of visited vertices
        visited = [False] * V
        # List to store the BFS traversal order
        bfs_order = []
        # Queue to manage the BFS process, starting with node 0
        queue = deque([0])
        # Mark the 0th node as visited
        visited[0] = True
        
        while queue:
            # Dequeue the front element
            node = queue.popleft()
            # Add the current node to the BFS order
            bfs_order.append(node)
            
            # Visit all the adjacent vertices of the dequeued node
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    # If not visited, mark as visited and enqueue
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        return bfs_order
