class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        min_heap = [(0, 0)]     #(dist, i)
        seen = set()
        ans = 0

        while len(seen) < n:
            dist, i = heapq.heappop(min_heap)

            if i in seen:
                continue

            seen.add(i)
            ans += dist
            xi, xj = points[i]

            for j in range(n):
                yi, yj = points[j]
                if j not in seen:
                    heapq.heappush(min_heap, (abs(xi-yi) + abs(xj-yj), j))
        
        return ans






        