class Solution:
    def isKPartitionPossible(self, a, k):
        n = len(a)
        total_sum = sum(a)
        
        # If total sum is not divisible by k, return False
        if total_sum % k != 0:
            return False
        
        target_sum = total_sum // k
        used = [False] * n
        
        def canPartition(start, k, current_sum):
            if k == 1:  # Only one partition left, no need to check further
                return True
            if current_sum == target_sum:
                return canPartition(0, k - 1, 0)
            for i in range(start, n):
                if not used[i] and current_sum + a[i] <= target_sum:
                    used[i] = True
                    if canPartition(i + 1, k, current_sum + a[i]):
                        return True
                    used[i] = False
            return False
        
        return canPartition(0, k, 0)
