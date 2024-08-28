from typing import List

class Solution:
    def countStudents(self, arr: List[int], pages: int) -> int:
        students = 1
        pagesStudent = 0
        
        for num in arr:
            if pagesStudent + num <= pages:
                pagesStudent += num
            else:
                students += 1
                pagesStudent = num
                
        return students

    def findPages(self, n: int, arr: List[int], m: int) -> int:
        if m > n:
            return -1
        
        low = max(arr)
        high = sum(arr)
        
        while low <= high:
            mid = (low + high) // 2
            students = self.countStudents(arr, mid)
            
            if students > m:
                low = mid + 1
            else:
                high = mid - 1
        
        return low
