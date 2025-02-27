from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, price in flights:
            graph[u].append((v, price))
                
        q = deque([(0, src, 0)])    # (price, node, stops)
        cost = [float('inf')] * n
        cost[src] = 0

        while q:
            price, node, stops = q.popleft()
            # if node == dst:
            #     return price

            if stops> k:
                continue
            
            for nei, wt in graph[node]:
                new_price = price + wt
                if new_price < cost[nei]:
                    cost[nei] = new_price
                    q.append((new_price, nei, stops+1))
        
        return cost[dst] if cost[dst] != float('inf') else -1


        
        