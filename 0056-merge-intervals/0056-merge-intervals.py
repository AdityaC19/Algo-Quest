class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        n = len(intervals)
        ans = [intervals[0]]

        for i in range(1, n):
            curr = ans[-1]
            if curr[1] >= intervals[i][0]:
                curr[1] = max(curr[1], intervals[i][1])
            else:
                ans.append(intervals[i])
        
        return ans
        