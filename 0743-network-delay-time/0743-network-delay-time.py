class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        min_heap = [(0, k)] #(dist, i)
        hmap = {} #(dist, node)

        graph = defaultdict(list)

        for u, v, wt in times:
            graph[u].append((v, wt))

        while min_heap:
            wt, i = heapq.heappop(min_heap)

            if i in hmap:
                continue
            
            hmap[i] = wt

            for nei_node in graph[i]:
                nei, new_wt = nei_node
                heapq.heappush(min_heap, (wt + new_wt , nei))
        
        if len(hmap) == n:
            return max(hmap.values())
        else:
            return -1

            
        


        