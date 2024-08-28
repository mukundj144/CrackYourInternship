from typing import List

class Solution:
    def knightDialer(self, n: int) -> int:
        # Define the knight moves for each keypad digit
        moves = {
            0: [4, 6],
            1: [8, 6],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        
        # Initialize the DP table
        dp = [[0] * 10 for _ in range(n)]
        
        # Base case: Length 1, each digit is itself
        for i in range(10):
            dp[0][i] = 1
        
        # Fill the DP table
        for length in range(1, n):
            for digit in range(10):
                for move in moves[digit]:
                    dp[length][digit] += dp[length - 1][move]
        
        # Calculate the total number of distinct phone numbers of length n
        return sum(dp[n - 1]) % (10**9 + 7)
