from collections import defaultdict, deque
from typing import List

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # Step 1: Create a graph
        graph = defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Find the start of the array (an element with only one neighbor)
        start = None
        for node in graph:
            if len(graph[node]) == 1:
                start = node
                break
        
        # Step 3: Traverse the graph to reconstruct the array
        res = []
        visited = set()
        queue = deque([start])
        
        while queue:
            node = queue.popleft()
            res.append(node)
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
        
        return res
