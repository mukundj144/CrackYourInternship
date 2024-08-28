class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # Step 1: Build the tree using an adjacency list
        tree = [[] for _ in range(n)]
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        # Step 2: Initialize variables
        subtree_size = [0] * n
        answer = [0] * n
        total_distance = 0
        
        # Step 3: DFS to calculate the size of each subtree and total distance from root
        def dfs(node, parent):
            subtree_size[node] = 1
            for neighbor in tree[node]:
                if neighbor == parent:
                    continue
                answer[neighbor] = dfs(neighbor, node)
                subtree_size[node] += subtree_size[neighbor]
                answer[node] += answer[neighbor] + subtree_size[neighbor]
            return answer[node]
        
        # Step 4: Calculate sum of distances for the root node (node 0)
        dfs(0, -1)
        
        # Step 5: DFS to calculate distances for all nodes using the root's distances
        def dfs_propagate(node, parent):
            for neighbor in tree[node]:
                if neighbor == parent:
                    continue
                # Use parent's distance to calculate child's distance
                answer[neighbor] = answer[node] - subtree_size[neighbor] + (n - subtree_size[neighbor])
                dfs_propagate(neighbor, node)
        
        dfs_propagate(0, -1)
        
        return answer
