class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        min_heap = []

        for s, e in intervals:
            if min_heap and min_heap[0] <= s:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, e)
        
        return len(min_heap)