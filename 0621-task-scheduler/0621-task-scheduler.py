class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_heap = []
        
        for task in counter:
            heapq.heappush(max_heap, -counter[task])
        
        q = deque()  # [count, available_time]
        time = 0

        while max_heap or q:
            time += 1
            if max_heap:
                count = heapq.heappop(max_heap) + 1  
                if count < 0:
                    q.append([count, time + n])
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        
        return time
