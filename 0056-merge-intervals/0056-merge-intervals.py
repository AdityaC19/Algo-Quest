class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        ans = [intervals[0]]
        n = len(intervals)

        for i in range(n):
            curr = ans[-1]

            if curr[1] >= intervals[i][0]:
                curr[1] = max(curr[1], intervals[i][1])
            else:
                ans.append(intervals[i])
        
        return ans

        

        