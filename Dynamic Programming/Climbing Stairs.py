class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Initialize the base cases
        prev1, prev2 = 1, 2
        
        # Compute the number of ways for each step from 3 to n
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev1, prev2 = prev2, current
        
        return prev2
