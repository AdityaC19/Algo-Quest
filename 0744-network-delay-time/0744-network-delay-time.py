import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, time in times:
            graph[u].append((v, time))
        
        dist = [float('inf')] * (n+1)
        dist[k] = 0
        min_heap = [(0, k)]   # (time, node)

        while min_heap:
            time, node = heapq.heappop(min_heap)

            for nei, wt in graph[node]:
                new_dist = time + wt
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    heapq.heappush(min_heap, (new_dist, nei))
        
        max_time = max(dist[1:])
        return max_time if max_time != float('inf') else -1




        