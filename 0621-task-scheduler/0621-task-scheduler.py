class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_heap = []
        q = deque()
        intervals = 0

        for key, val in counter.items():
            heapq.heappush(max_heap, -val)
        
        while max_heap or q:
            intervals += 1
            if max_heap:
                freq =  heapq.heappop(max_heap)
                freq = -freq - 1

                if freq > 0:
                    q.append((freq, intervals + n))

            if q and q[0][1] == intervals:
                f = -q.popleft()[0]
                heapq.heappush(max_heap, f)

        return intervals
            





        