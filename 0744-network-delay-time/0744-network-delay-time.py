class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u,v,w in times:
            graph[u].append((v, w))
        
        dist = [(float('inf'))] * (n+1)
        dist[k] = 0
        min_heap = [(0, k)]     # (node, time)

        while min_heap:
            time, node = heapq.heappop(min_heap)

            for nei_node, wt in graph[node]:
                if time + wt < dist[nei_node]:
                    dist[nei_node] = time + wt
                    heapq.heappush(min_heap, (time+wt, nei_node))
        
        max_time = max(dist[1:])
        return max_time if max_time != float('inf') else -1
        