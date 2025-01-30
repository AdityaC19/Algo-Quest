import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        seen = set()
        min_heap = [(0,0)]
        total_cost = 0

        while min_heap:
            dist, i = heapq.heappop(min_heap)
            if i in seen:
                continue
            seen.add(i)
            total_cost += dist
            xi, yi = points[i]

            for j in range(n):
                if j not in seen:
                    xj, yj = points[j]
                    nei_dist = abs(xi-xj) + abs(yi-yj)
                    heapq.heappush(min_heap, (nei_dist, j))
                    #total_cost += nei_dist
        
        return total_cost


            




        