class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        for interval in intervals:
            # new Interval is after curr interval
            if interval[1] < newInterval[0]:
                ans.append(interval)
            # new Interval is before curr interval
            elif interval[0] > newInterval[1]:
                ans.append(newInterval)
                newInterval = interval
            #overlapping
            elif interval[1] >= newInterval[0] or interval[0] <= newInterval[1]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
        
        ans.append(newInterval)

        return ans

        