from typing import List

class Solution:
    # Helper function for DFS to perform topological sorting
    def topo_sort(self, node, visited, stack, adj):
        visited[node] = True
        for neighbour in adj[node]:
            if not visited[neighbour]:
                self.topo_sort(neighbour, visited, stack, adj)
        # Push the node to stack once all its adjacent nodes are processed
        stack.append(node)

    # Function to return list containing vertices in Topological order
    def topoSort(self, V, adj: List[List[int]]) -> List[int]:
        # Initialize visited list and stack
        visited = [False] * V
        stack = []

        # Call DFS for all nodes
        for i in range(V):
            if not visited[i]:
                self.topo_sort(i, visited, stack, adj)
    
        # Return topological order by reversing the stack
        return list(reversed(stack))

