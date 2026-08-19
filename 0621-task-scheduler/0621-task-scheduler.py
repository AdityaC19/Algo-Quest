class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_heap = []
        cooldown = deque()  # (task ,available time)
        time = 0

        for task in counter:
            heapq.heappush(max_heap, -counter[task])
        
        while max_heap or cooldown:
            time += 1
            if max_heap:
                task = -heapq.heappop(max_heap) - 1
                if task > 0:
                    cooldown.append((task, time+n))
            
            if cooldown and cooldown[0][1] == time:
                task_count = cooldown.popleft()[0]
                heapq.heappush(max_heap, -task_count)
        
        return time


        