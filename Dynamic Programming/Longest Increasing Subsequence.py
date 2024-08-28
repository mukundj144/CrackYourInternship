import bisect

class Solution:
    def solveOptimal(self, n: int, a: List[int]) -> int:
        if n == 0:
            return 0

        ans = []
        ans.append(a[0])
        
        for i in range(1, n):
            if a[i] > ans[-1]:
                # If the current element is greater than the last element in ans, append it
                ans.append(a[i])
            else:
                # Otherwise, find the position of the smallest element in ans that is >= a[i]
                index = bisect.bisect_left(ans, a[i])
                # Replace that element with a[i] to maintain the smallest possible end element
                ans[index] = a[i]
        
        # The length of ans is the length of the LIS
        return len(ans)
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        return self.solveOptimal(n, nums)
