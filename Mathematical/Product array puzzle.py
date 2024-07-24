class Solution:
    def productExceptSelf(self, nums,n):
        left = [0] * n
        right = [0] * n
        res = [0] * n

        left[0] = 1
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        right[n - 1] = 1
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        for i in range(n):
            res[i] = left[i] * right[i]

        return res 