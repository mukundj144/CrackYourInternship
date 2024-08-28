from typing import List

class Solution:
    def solveMem(self, i: int, j: int, mat: List[List[int]], dp: List[List[int]]) -> int:
        if i >= len(mat) or j >= len(mat[0]):
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        if mat[i][j] == 1:
            right = self.solveMem(i, j + 1, mat, dp)
            diagonal = self.solveMem(i + 1, j + 1, mat, dp)
            down = self.solveMem(i + 1, j, mat, dp)
            dp[i][j] = 1 + min(right, diagonal, down)
        else:
            dp[i][j] = 0
        
        return dp[i][j]
        
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        n = len(matrix)
        m = len(matrix[0])
        
        dp = [[-1] * m for _ in range(n)]
        total_squares = 0
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                total_squares += self.solveMem(i, j, matrix, dp)
        
        return total_squares
