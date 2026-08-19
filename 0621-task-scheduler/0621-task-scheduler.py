class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_heap = []   #(freq)
        wait_q = deque()    #(tasks, when available time)
        time = 0

        for task in counter:
            heapq.heappush(max_heap, -counter[task])
        
        while max_heap or wait_q:
            time += 1
            if max_heap:
                task = heapq.heappop(max_heap)
                task = -task - 1

                if task > 0:
                    wait_q.append((task, time + n))
            
            if wait_q and wait_q[0][1] == time:
                task_count = wait_q.popleft()[0]
                heapq.heappush(max_heap, -task_count)
        
        return time


                

        