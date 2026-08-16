class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        hmap = {}
        min_heap = [(0, k)] #(wt, src)

        graph = defaultdict(list)

        for u,v,wt in times:
            graph[u].append((v, wt))

        while min_heap:
            wt, node = heapq.heappop(min_heap)   

            if node in hmap:
                continue

            hmap[node] = wt

            for nei_node, nei_wt in graph[node]:
                #if nei_node not in hmap:
                heapq.heappush(min_heap, (wt + nei_wt, nei_node))    
        
        if len(hmap) == n:
            return max(hmap.values())
        else:
            return -1