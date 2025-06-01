class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]

        for interval in intervals:
            curr = ans[-1]

            if curr[1] >= interval[0]:
                curr[1] = max(curr[1], interval[1])
            else:
                ans.append(interval)
        
        return ans
        