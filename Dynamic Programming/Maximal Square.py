from typing import List

class Solution:
    def solveMem(self, i: int, j: int, mat: List[List[str]], dp: List[List[int]], maxi: List[int]) -> int:
        if i >= len(mat) or j >= len(mat[0]):
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        right = self.solveMem(i, j + 1, mat, dp, maxi)
        diagonal = self.solveMem(i + 1, j + 1, mat, dp, maxi)
        down = self.solveMem(i + 1, j, mat, dp, maxi)
        
        if mat[i][j] == '1':
            dp[i][j] = 1 + min(right, min(diagonal, down))
            maxi[0] = max(maxi[0], dp[i][j])
        else:
            dp[i][j] = 0
        
        return dp[i][j]

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        n = len(matrix)
        m = len(matrix[0])
        
        dp = [[-1] * m for _ in range(n)]
        maxi = [0]  # Use a list to mutate the variable inside solveMem
        
        self.solveMem(0, 0, matrix, dp, maxi)
        
        return maxi[0] * maxi[0]
