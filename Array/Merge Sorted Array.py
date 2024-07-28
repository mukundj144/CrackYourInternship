from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Create a copy of the first m elements of nums1
        a = nums1[:m]
        
        # Pointers for nums1 (a), nums2, and the merged array (nums1)
        i = 0  # pointer for a
        j = 0  # pointer for nums2
        k = 0  # pointer for nums1 (merged array)
        
        # Merge the two arrays
        while i < m and j < n:
            if a[i] < nums2[j]:
                nums1[k] = a[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        
        # Copy the remaining elements from a, if any
        while i < m:
            nums1[k] = a[i]
            i += 1
            k += 1
        
        # Copy the remaining elements from nums2, if any
        while j < n:
            nums1[k] = nums2[j]
            j += 1
            k += 1

