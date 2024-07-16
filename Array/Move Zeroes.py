class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero_at=0

        for i in range(len(nums)):
            if nums[i]!=0:
                nums[last_non_zero_at]=nums[i]
                last_non_zero_at +=1

        for i in range(last_non_zero_at,len(nums)):
            nums[i]=0        