class Solution:
    def func(self, n, x, y, z):
        if n == 0:
            return 0
        if n in self.dp:
            return self.dp[n]

        op1 = op2 = op3 = float('-inf')

        if n >= x:
            op1 = self.func(n - x, x, y, z)
        if n >= y:
            op2 = self.func(n - y, x, y, z)
        if n >= z:
            op3 = self.func(n - z, x, y, z)

        self.dp[n] = 1 + max(op1, op2, op3)
        return self.dp[n]

    # Function to find the maximum number of cuts.
    def maximizeTheCuts(self, n, x, y, z):
        self.dp = {}
        result = self.func(n, x, y, z)
        return max(result, 0)  # If result is negative, return 0.
