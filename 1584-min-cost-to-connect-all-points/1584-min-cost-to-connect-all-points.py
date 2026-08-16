class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        min_heap = [(0,0)]  # (dist, i)
        seen = set()
        total_cost = 0
        
        while len(seen) < n:
            dist , i = heapq.heappop(min_heap)

            if i in seen:
                continue
            
            seen.add(i)
            total_cost += dist
            xi, yi = points[i]

            for j in range(n):
                if j not in seen:   # (neighboring points)
                    xj, yj = points[j]
                    new_dist = abs(xi - xj) + abs(yi - yj)
                    heapq.heappush(min_heap, (new_dist, j))
        
        return total_cost


        