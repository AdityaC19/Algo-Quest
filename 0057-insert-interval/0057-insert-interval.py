class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        for interval in intervals:
            # if new comes after curr
            if interval[1] < newInterval[0]:
                ans.append(interval)
            # if new comes before curr
            elif interval[0] > newInterval[1]:
                ans.append(newInterval)
                newInterval = interval
            
            # overlapping intervals
            elif interval[1] > newInterval[0] or interval[0] < newInterval[1]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
        
        ans.append(newInterval)

        return ans
            


        