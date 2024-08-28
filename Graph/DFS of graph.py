class Solution:
    # Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # List to keep track of visited nodes
        visited = [False] * V
        # List to store the DFS traversal order
        dfs_order = []
        
        # Helper function to perform DFS recursively
        def dfs(node):
            # Mark the current node as visited
            visited[node] = True
            # Add the node to the DFS traversal list
            dfs_order.append(node)
            
            # Recur for all unvisited adjacent vertices
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
        
        # Start DFS from node 0
        dfs(0)
        
        return dfs_order
