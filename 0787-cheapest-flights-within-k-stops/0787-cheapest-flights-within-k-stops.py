class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        min_heap = [(0, src, 0)] # (price, src, k)
        hmap = defaultdict(int)

        graph = defaultdict(list)

        for u, v, wt in flights:
            graph[u].append((v, wt))
        
        while min_heap:
            price, i, stops = heapq.heappop(min_heap)

            if i == dst:
                return price

            if stops > k:
                continue
                
            for nei_node, wt in graph[i]:
                new_price = price + wt
                if (nei_node, stops) not in hmap or new_price < hmap[(nei_node, stops)]:
                    hmap[(nei_node, stops)] = new_price
                    heapq.heappush(min_heap, (new_price, nei_node,  stops+1))
        
        return -1

        
        

