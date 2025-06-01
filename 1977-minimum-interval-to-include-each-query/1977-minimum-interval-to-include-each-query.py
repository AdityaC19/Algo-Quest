class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        min_heap = []

        i = 0
        hmap = {}

        for q in sorted(queries):
            # push into min heap when q lies in the interval
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(min_heap, (r-l+1, r))
                i += 1
            
            # pop from min heap when q is larger than interval end value i.e. min_heap[0][1]
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            hmap[q] = min_heap[0][0] if min_heap else -1
        
        return [hmap[q] for q in queries]

        