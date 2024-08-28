class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Step 1: Sort intervals based on the end time
        intervals.sort(key=lambda x: x[1])
        
        # Initialize count and lastEndTime
        cnt = 1
        last = intervals[0][1]
        
        # Step 2: Iterate through the intervals starting from the second one
        for i in range(1, len(intervals)):
            if intervals[i][0] >= last:
                cnt += 1
                last = intervals[i][1]
        
        # Return the number of intervals that need to be removed
        return len(intervals) - cnt

