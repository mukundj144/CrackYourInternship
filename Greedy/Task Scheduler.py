import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = []
        
        # Push each negated count into the maxHeap individually
        for cnt in count.values():
            heapq.heappush(maxHeap, -cnt)
        
        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        
        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time
