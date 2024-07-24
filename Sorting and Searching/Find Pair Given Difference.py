from typing import List

class Solution:
    def findPair(self, n: int, x: int, arr: List[int]) -> int:
        arr.sort()
       
        left = 0
        right = 1
        
        while right < n:
            
            diff = arr[right] - arr[left]
            
            if diff == x:
                return 1
                
            elif diff < x:
                right += 1
                
            else:
                left += 1
            
            if left == right:
                right += 1
        
        return -1        

