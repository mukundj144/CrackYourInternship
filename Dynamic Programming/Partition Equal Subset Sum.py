class Solution:
    def solveMem(self, index, arr, N, target, dp):
        # Base cases
        if index >= N:
            return False
        if target < 0:
            return False
        if target == 0:
            return True

        # Check if solution already exists in dp array
        if dp[index][target] != -1:
            return dp[index][target]

        # Recursively check including or excluding the current element
        incl = self.solveMem(index + 1, arr, N, target - arr[index], dp)
        excl = self.solveMem(index + 1, arr, N, target, dp)

        # Store the result in dp array
        dp[index][target] = incl or excl
        return dp[index][target]

    def equalPartition(self, N, arr):
        total = sum(arr)
        
        # If total sum is odd, partitioning into two equal parts is impossible
        if total % 2 != 0:
            return False
        
        # We need to check if there exists a subset with sum equal to total//2
        target = total // 2
        
        # Initialize dp array with -1, meaning uncomputed state
        dp = [[-1 for _ in range(target + 1)] for _ in range(N)]
        
        # Start the recursive function with memoization
        return self.solveMem(0, arr, N, target, dp)
