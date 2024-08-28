class Solution:
    def sum_freq(self, i, j, freq):
        # Calculate the sum of frequencies from index i to j
        total_sum = 0
        for k in range(i, j + 1):
            total_sum += freq[k]
        return total_sum

    def cost(self, i, j, freq):
        # Base case: No keys
        if i > j:
            return 0

        # Base case: Single key
        if i == j:
            return freq[i]

        # If the value is already computed, return it
        if self.dp[i][j] != -1:
            return self.dp[i][j]

        # Calculate the sum of frequencies
        weight = self.sum_freq(i, j, freq)
        ans = float('inf')

        # Try every possible root and find the minimum cost
        for k in range(i, j + 1):
            temp = self.cost(i, k - 1, freq) + self.cost(k + 1, j, freq)
            ans = min(temp, ans)

        # Store the computed result in dp array
        self.dp[i][j] = ans + weight
        return self.dp[i][j]

    def optimalSearchTree(self, keys, freq, n):
        self.dp = [[-1 for _ in range(n)] for _ in range(n)]
        # Compute the cost of the optimal search tree
        return self.cost(0, n - 1, freq)

