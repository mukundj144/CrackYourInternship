class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()

        mid = len(nums)//2
        count = 0
        for num in nums:
            count += abs(nums[mid]-num)
        
        return count