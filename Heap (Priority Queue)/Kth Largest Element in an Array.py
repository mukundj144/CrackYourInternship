import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Initialize a min-heap
        min_heap = []
        
        # Iterate over each number in the list
        for num in nums:
            heapq.heappush(min_heap, num)  # Push the current number onto the heap
            
            # If the size of the heap exceeds k, pop the smallest element
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # The root of the heap is the k-th largest element
        return min_heap[0]
