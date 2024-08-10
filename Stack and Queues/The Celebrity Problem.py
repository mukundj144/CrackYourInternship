class Solution:
    def celebrity(self, mat):
        # code here
        n=len(mat)
        knowMe=[0]*n
        Iknow=[0]*n
    
        for i in range(n):
            for j in range(n):
                if mat[i][j]==1:
                    knowMe[j]+=1
                    Iknow[i]+=1
                    
        for i in range(n):
            if knowMe[i]==n-1 and Iknow[i]==0:
                return i
        return -1   