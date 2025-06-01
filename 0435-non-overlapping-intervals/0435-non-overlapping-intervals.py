class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 1
        intervals.sort(key = lambda x: x[1])
        n = len(intervals)

        prev = 0

        for i in range(1,n):
            # if start time of curr meeting > end time of prev meeting
            if intervals[i][0] >= intervals[prev][1]:
                # set prev to curr idx i
                prev = i
                # increment safe meetings counter by 1
                count += 1
                
        return n - count 
        