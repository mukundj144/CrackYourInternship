import heapq
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)  # Number of rows (and columns)
        min_heap = []  # Initialize the min-heap
        
        # Initialize the heap with the first element of each row
        for r in range(n):
            heapq.heappush(min_heap, (matrix[r][0], r, 0))
        
        # Extract the minimum element from the heap k times
        for _ in range(k):
            val, r, c = heapq.heappop(min_heap)
            
            # If it's the k-th smallest element, return it
            if _ == k - 1:
                return val
            
            # Push the next element in the same row if available
            if c + 1 < n:
                heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))
