from collections import defaultdict
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Sort the array
        res = []
        n = len(nums)
        
        for i in range(n):
            # Avoid duplicates for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i + 1, n):
                # Avoid duplicates for the second element
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                
                left, right = j + 1, n - 1
                
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        
                        # Avoid duplicates for the third element
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        
                        # Avoid duplicates for the fourth element
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        
        return res