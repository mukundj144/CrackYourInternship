from typing import List

class Solution:
    def findOrder(self, dict: List[str], N: int, K: int) -> str:
        adj = [[] for _ in range(K)]
        
        for i in range(N - 1):
            s1 = dict[i]
            s2 = dict[i + 1]
            length = min(len(s1), len(s2))
            for ptr in range(length):
                if s1[ptr] != s2[ptr]:
                    adj[ord(s1[ptr]) - ord('a')].append(ord(s2[ptr]) - ord('a'))
                    break
        
        # Topological sort
        visited = [False] * K
        stack = []
        
        def topo_sort(node):
            visited[node] = True
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    topo_sort(neighbour)
            stack.append(node)
        
        for i in range(K):
            if not visited[i]:
                topo_sort(i)
        
        ans = ""
        while stack:
            ans += chr(stack.pop() + ord('a'))
        
        return ans
