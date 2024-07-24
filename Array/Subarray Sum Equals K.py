class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix_sums = {0: 1}  # Initialize with 0:1 to handle subarrays starting from index 0
        
        for num in nums:
            current_sum += num
            
            # Check if there's a prefix sum that matches the required value
            if current_sum - k in prefix_sums:
                count += prefix_sums[current_sum - k]
            
            # Update the prefix sums dictionary
            if current_sum in prefix_sums:
                prefix_sums[current_sum] += 1
            else:
                prefix_sums[current_sum] = 1
        
        return count     