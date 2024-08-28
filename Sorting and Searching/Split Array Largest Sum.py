from typing import List

class Solution:
    def countStudents(self, nums: List[int], pages: int) -> int:
        students = 1
        pagesStudent = 0
        
        for num in nums:
            if pagesStudent + num <= pages:
                pagesStudent += num
            else:
                students += 1
                pagesStudent = num
                
        return students

    def splitArray(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1
        
        low = max(nums)  # Maximum element in nums
        high = sum(nums)  # Sum of all elements in nums
        
        while low <= high:
            mid = (low + high) // 2
            students = self.countStudents(nums, mid)
            
            if students > k:
                low = mid + 1
            else:
                high = mid - 1
        
        return low
