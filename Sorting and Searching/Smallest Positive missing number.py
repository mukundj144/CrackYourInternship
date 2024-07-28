class Solution:
    
    # Function to find the smallest positive number missing from the array.
    def missingNumber(self, arr, n):
        # Sort the array
        arr.sort()
        
        # Initialize the smallest positive number we expect to find
        smallest_missing = 1
        
        # Iterate through the array
        for num in arr:
            # Only consider positive numbers
            if num == smallest_missing:
                smallest_missing += 1
        
        return smallest_missing
