class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        min_heap = [(0, k)] # (dist from sourse to node, node)
        min_times = {}
        
        graph = defaultdict(list)

        for u, v, time in times:
            graph[u].append((v,time))
        
        while min_heap:
            time, i = heapq.heappop(min_heap)
            if i in min_times:
                continue
            min_times[i] = time

            for nei, nei_time in graph[i]:
                if nei not in min_times:
                    heapq.heappush(min_heap, (time+nei_time, nei))
        
        if len(min_times) == n:
            return max(min_times.values())
        else:
            return -1
