class Solution:
    def getCount(self, n):
        if n == 1:
            return 10  # There are 10 digits on the keypad

        # The neighbors mapping based on the allowed movements
        neighbors = {
            0: [0, 8],
            1: [1, 2, 4],
            2: [2, 1, 3, 5],
            3: [3, 2, 6],
            4: [4, 1, 5, 7],
            5: [5, 2, 4, 6, 8],
            6: [6, 3, 5, 9],
            7: [7, 4, 8],
            8: [8, 0, 5, 7, 9],
            9: [9, 6, 8]
        }

        # Initialize dp for the first length (n=1)
        dp = [[0] * 10 for _ in range(n)]
        for i in range(10):
            dp[0][i] = 1

        # Fill the DP table for lengths from 2 to n
        for length in range(1, n):
            for digit in range(10):
                dp[length][digit] = sum(dp[length - 1][neighbor] for neighbor in neighbors[digit])

        # The final answer is the sum of all possible sequences of length n
        return sum(dp[n - 1][digit] for digit in range(10))
