class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, subset):
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
            result.append(subset[:])    
        
        nums.sort()  # Sort to handle duplicates
        result = []
        backtrack(0, [])
        return result