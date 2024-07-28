from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # Initialize a dictionary to keep count of elements
        hashmap = {}
        # List to store duplicate elements
        dupl = []
        
        # Iterate through each number in the list
        for num in nums:
            # If the number is already in the hashmap, increment its count
            if num in hashmap:
                hashmap[num] += 1
            # If the number is not in the hashmap, add it with a count of 1
            else:
                hashmap[num] = 1
        
        # Iterate through the hashmap to find duplicates
        for key, value in hashmap.items():
            if value > 1:
                dupl.append(key)
        
        return dupl