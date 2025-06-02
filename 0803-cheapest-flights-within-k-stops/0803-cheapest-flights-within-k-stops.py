class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, price in flights:
            graph[u].append((v,price))
        
        min_heap = [(0, src, 0)]  # (price, node, stops)
        cost = defaultdict(int) # key=node, stops    val=cost

        while min_heap:
            price, node, stops = heapq.heappop(min_heap)
            if node == dst:
                return price
            if stops > k:
                continue
            for nei_node, wt in graph[node]:
                new_cost = price + wt
                if (nei_node, stops) not in cost or new_cost < cost[(nei_node, stops)] :
                    cost[(nei_node, stops)] = new_cost
                    heapq.heappush(min_heap, (new_cost, nei_node, stops+1))
        
        return -1

            
        