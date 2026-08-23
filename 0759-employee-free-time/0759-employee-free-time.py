"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        ints = []
        for event in schedule:
            for e in event:
                ints.append(e)
        
        ints.sort(key=lambda x:x.start)

        merged = []
        for i in ints:
            if not merged or i.start > merged[-1].end:
                merged.append(i)
            else:
                merged[-1].end = max(merged[-1].end, i.end)
        
        free = []
        for i in range(1, len(merged)):
            free.append(Interval(merged[i-1].end, merged[i].start))
        
        return free
        


