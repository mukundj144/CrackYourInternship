class Solution:
	def shortest_distance(self, matrix):
		#Code here
		n=len(matrix)
		
		for i in range(n):
		    for j in range(n):
                if matrix[i][j]==-1:
                    matrix[i][j]=float('inf')
                if i==j:
                    matrix[i][i]=0   
                    
       # Floyd-Warshall algorithm to find shortest paths
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][k] < float('inf') and matrix[k][j] < float('inf'):
                        matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
                    
        for i in range(n):
		    for j in range(n):
                if matrix[i][j]==float('inf'):
                    matrix[i][j]=-1