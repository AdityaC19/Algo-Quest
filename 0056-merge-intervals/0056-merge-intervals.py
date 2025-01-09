class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            last_interval = ans[-1]

            if last_interval[1] >= intervals[i][0]:
                last_interval[1] = max(last_interval[1], intervals[i][1])
            else:
                ans.append(intervals[i])
        
        return ans

   