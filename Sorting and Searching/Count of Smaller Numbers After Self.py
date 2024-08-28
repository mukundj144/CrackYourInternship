from typing import List, Tuple

class Solution:
    def merge(self, nums_pair: List[Tuple[int, int]], temp: List[Tuple[int, int]], left: int, mid: int, right: int, ans: List[int]):
        i, j, k = left, mid + 1, left
        
        # Merging two halves while counting the smaller elements on the right
        while i <= mid and j <= right:
            if nums_pair[i][0] <= nums_pair[j][0]:
                temp[k] = nums_pair[j]
                j += 1
            else:
                ans[nums_pair[i][1]] += right - j + 1
                temp[k] = nums_pair[i]
                i += 1
            k += 1
        
        # Copying the remaining elements from the left half
        while i <= mid:
            temp[k] = nums_pair[i]
            i += 1
            k += 1
        
        # Copying the remaining elements from the right half
        while j <= right:
            temp[k] = nums_pair[j]
            j += 1
            k += 1
        
        # Copying the sorted subarray back into the original array
        for i in range(left, right + 1):
            nums_pair[i] = temp[i]

    def merge_sort_and_count(self, nums_pair: List[Tuple[int, int]], temp: List[Tuple[int, int]], left: int, right: int, ans: List[int]):
        if left < right:
            mid = (left + right) // 2
            
            # Sort the left half
            self.merge_sort_and_count(nums_pair, temp, left, mid, ans)
            
            # Sort the right half
            self.merge_sort_and_count(nums_pair, temp, mid + 1, right, ans)
            
            # Merge the two halves and count the smaller elements
            self.merge(nums_pair, temp, left, mid, right, ans)

    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums_pair = [(num, i) for i, num in enumerate(nums)]
        temp = [0] * n
        ans = [0] * n
        
        # Perform merge sort and count the smaller elements
        self.merge_sort_and_count(nums_pair, temp, 0, n - 1, ans)
        
        return ans
