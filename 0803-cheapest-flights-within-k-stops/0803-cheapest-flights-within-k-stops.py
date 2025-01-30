from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, price in flights:
            graph[u].append((v, price))
            #graph[v].append((u, price))
        
        min_heap = [(0, src, 0)]
        #q.append((0, src, 0))
        seen = defaultdict(int)

        while min_heap:
            price, i, stops = heapq.heappop(min_heap)
            if i == dst: 
                return price
            
            if stops > k:
                continue

            for nei, nei_price in graph[i]:
                new_price = price + nei_price
                if (nei, stops) not in seen or new_price < seen[(nei, stops)]:
                    seen[(nei, stops)] = new_price
                    heapq.heappush(min_heap, (new_price, nei, stops+1))
                    #print(min_heap)
        
        return -1



        

        # while min_heap:
        #     price, i = heapq.heappop(min_heap)
        #     if i in seen:
        #         continue
        #     seen[i] = price

        #     # for j in range(k):
        #     #     if j not in seen:
        #     #         heapq.heappush(min_heap, ())

        #     for nei, nei_price in graph[i]:
        #         if nei not in seen:
        #             heapq.heappush(min_heap, (nei_price+price, nei))
        
        # print(seen)
