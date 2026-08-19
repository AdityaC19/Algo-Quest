class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key= lambda x:x[1])

        prev = 0
        count = 1

        if intervals == []: return True

        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[prev][1]:
                prev = i
                count += 1
        
        return True if count == len(intervals) else False
        