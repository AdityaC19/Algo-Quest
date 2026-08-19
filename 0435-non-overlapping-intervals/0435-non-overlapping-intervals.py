class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        curr = intervals[0]
        count = 0

        for i in range(1, len(intervals)):
            if curr[1] > intervals[i][0]:
                count += 1
                curr = min(curr, intervals[i], key=lambda x:x[1])
            else:
                curr = intervals[i]
        
        return count

        