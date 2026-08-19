class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x:x[1])
        n = len(intervals)
        count =1 
        prev = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[prev][1]:
                prev = i
                count += 1
        
        return n-count


        # intervals.sort()
        # curr = intervals[0]
        # count = 0

        # for i in range(1, len(intervals)):
        #     if curr[1] > intervals[i][0]:
        #         count += 1
        #         curr = min(curr, intervals[i], key=lambda x:x[1])
        #     else:
        #         curr = intervals[i]
        
        # return count

        