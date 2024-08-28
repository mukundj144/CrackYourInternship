from typing import List

class Solution:
    def solve(self, index: int, operationNo: int, k: int, prices: List[int], dp: List[List[int]]) -> int:
        # Base case: If we are out of days or no transactions left
        if index >= len(prices) or operationNo >= 2 * k:
            return 0
        
        # If this state has been computed before, return the stored result
        if dp[index][operationNo] != -1:
            return dp[index][operationNo]
        
        # Initialize profit
        profit = 0
        
        if operationNo % 2 == 0:
            # Buy allowed
            buyKaro = -prices[index] + self.solve(index + 1, operationNo + 1, k, prices, dp)
            skipKaro = self.solve(index + 1, operationNo, k, prices, dp)
            profit = max(buyKaro, skipKaro)
        else:
            # Sell allowed
            sellKaro = prices[index] + self.solve(index + 1, operationNo + 1, k, prices, dp)
            skipKaro = self.solve(index + 1, operationNo, k, prices, dp)
            profit = max(sellKaro, skipKaro)
        
        # Store and return the result
        dp[index][operationNo] = profit
        return profit

    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1] * (2 * k) for _ in range(n)]
        return self.solve(0, 0, k, prices, dp)
