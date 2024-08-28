from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize the dp array with -1 for memoization
        dp = [-1] * (amount + 1)
        
        # Call the helper function for the initial amount
        result = self.solveMem(coins, amount, dp)
        
        # Return the result; if it's infinity, return -1 as per the problem statement
        return result if result != float('inf') else -1

    def solveMem(self,coins: List[int], x: int, dp: List[int]) -> int:
        # Base case
        if x == 0:
            return 0
        if x < 0:
            return float('inf')
        if dp[x] != -1:
            return dp[x]
        
        mini = float('inf')
        for coin in coins:
            ans = self.solveMem(coins, x - coin, dp)
            if ans != float('inf'):
                mini = min(mini, 1 + ans)
        
        dp[x] = mini
        return mini
