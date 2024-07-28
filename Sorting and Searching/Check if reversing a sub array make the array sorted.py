class Solution:
    def canBeSortedByReversingSubarray(self, arr):
        n = len(arr)
        
        # Function to check if the array is sorted
        def isSorted(arr):
            for i in range(1, len(arr)):
                if arr[i] > arr[i - 1]:
                    return True
            return False

        # If the array is already sorted, return "Yes"
        if isSorted(arr):
            return "Yes"

        # Find the first decreasing segment
        l, r = 0, n - 1
        while l < n - 1 and arr[l] <= arr[l + 1]:
            l += 1
        while r > 0 and arr[r] >= arr[r - 1]:
            r -= 1

        # Reverse the subarray arr[l:r+1]
        subarray_reversed = arr[:l] + arr[l:r+1][::-1] + arr[r+1:]

        # Check if the array is sorted after reversing the subarray
        if isSorted(subarray_reversed):
            return "Yes"
        else:
            return "No"

# Driver code 
arr = [1, 2, 5, 4, 3] 
solution = Solution() 
if solution.canBeSortedByReversingSubarray(arr) == "Yes": 
    print("Yes") 
else: 
    print("No")
