class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        seen = set()
        min_heap = [(0,0)]  #(dist, node)
        cost = [float('inf')] * n
        res = 0

        while len(seen) < n:
            dist, i = heapq.heappop(min_heap)
            if i in seen:
                continue
            seen.add(i)
            res += dist
            xi, yi = points[i]

            for j in range(n):
                if j not in seen:
                    xj, yj = points[j]
                    new_dist = abs(xi-xj) + abs(yi-yj)
                    if new_dist < cost[j]:
                        cost[j] = new_dist
                        heapq.heappush(min_heap, (new_dist, j))
        
        return res

            
        