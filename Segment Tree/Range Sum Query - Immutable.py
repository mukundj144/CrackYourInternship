class NumArray:

    def __init__(self, nums: List[int]):
        self.cumulative_sum = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            self.cumulative_sum[i] = self.cumulative_sum[i - 1] + nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        return self.cumulative_sum[right + 1] - self.cumulative_sum[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)