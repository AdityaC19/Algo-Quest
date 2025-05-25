class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, price in flights:
            graph[u].append((v, price))
        
        cost = [float('inf')] * (n+1)
        cost[src] = 0
        q = deque([(0, src, 0)])    # (price, node, stops)

        while q:
            price, node, stops = q.popleft()

            if stops > k:
                continue

            for nei_node, wt in graph[node]:
                new_price = price + wt
                if new_price < cost[nei_node]:
                    cost[nei_node] = new_price
                    q.append((new_price, nei_node, stops+1))
                    print(q)
        
        return cost[dst] if cost[dst] != float('inf') else -1