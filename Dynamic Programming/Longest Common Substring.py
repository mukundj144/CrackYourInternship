#User function Template for python3

class Solution:
    def longestCommonSubstr(self, str1: str, str2: str) -> int:
        m = len(str1)
        n = len(str2)
        
        # Initialize the DP table
        c = [[0] * (n + 1) for _ in range(m + 1)]
        max_length=0
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    c[i][j] = 1 + c[i - 1][j - 1]
                    max_length = max(c[i][j], max_length)
                else:
                    c[i][j] = 0
        
        # The length of the longest common substring
        return max_length
