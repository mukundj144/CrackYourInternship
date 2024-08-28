import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Min-Heap to store the closest points
        max_heap = []
        
        for x, y in points:
            # Calculate the negative Euclidean distance
            distance = -(x**2 + y**2)
            
            # Push the point with its negative distance into the heap
            heapq.heappush(max_heap, (distance, [x, y]))
            
            # If the heap exceeds k elements, remove the farthest point
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        # Return the k closest points
        return [point for _, point in max_heap]
