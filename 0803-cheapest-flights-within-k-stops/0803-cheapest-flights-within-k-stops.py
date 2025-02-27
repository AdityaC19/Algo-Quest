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



# from collections import defaultdict, deque
# from typing import List

# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         graph = defaultdict(list)

#         for u, v, price in flights:
#             graph[u].append((v, price))
        
#         stk = []
#         def topoSort(node):
#             visited[node] = 1
            
#             for nei in graph[node]:
#                 v = nei[0]
#                 if not visited[v]:
#                     topoSort(v)

#             stk.append(node)

#         visited = [0] * n
#         for i in range(n):
#             if not visited[i]:
#                 topoSort(i)
        
#         dist = [float('inf')] * n
#         dist[src] = 0  # Source node distance is 0

#         while stk:
#             node = stk.pop()

#             if dist[node] != float('inf'):  
#                 for nei in graph[node]:
#                     v, price = nei
#                     if dist[node] + price < dist[v]:
#                         dist[v] = dist[node] + price

#         return dist[dst] if dist[dst] != float('inf') else -1
