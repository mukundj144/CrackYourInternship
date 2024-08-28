import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        minheap=[1]
        visited=set()
        factor=[2,3,5]

        for i in range(n):
            num=heapq.heappop(minheap)
            if i==n-1:
                return num
            for f in factor:
                if num*f not in visited:
                    visited.add(num*f)
                    heapq.heappush(minheap,num*f)
                            
