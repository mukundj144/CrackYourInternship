class Solution:
     # Function to find the minimum number of swaps required to sort the array.
    def minSwaps(self, nums):
        n = len(nums)
        
        if nums == sorted(nums):
            return 0
        
        sorted_nums = sorted(nums)
        
        index_map = {value: index for index, value in enumerate(sorted_nums)}
        
        swaps = 0
        for i in range(n):
            while nums[i] != sorted_nums[i]:
                correct_index = index_map[nums[i]]
                
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
                
                swaps += 1
        
        return swaps