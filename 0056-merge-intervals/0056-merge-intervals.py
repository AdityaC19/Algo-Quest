class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        ans = [intervals[0]]
        n = len(intervals)

        for i in range(1, n):
            cur_interval = ans[-1]

            if cur_interval[1] >= intervals[i][0]:
                cur_interval[1] = max(cur_interval[1], intervals[i][1])
            else:
                ans.append(intervals[i])
        
        return ans


        