class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D dp array with all elements initialized to 1
        dp = [[1] * n for _ in range(m)]
        
        # Fill the dp array
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # The answer is in the bottom-right corner of the grid
        return dp[m-1][n-1]
