class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        min_heap = [(0, 0, 0)]  # (effort, i, j)
        dist = defaultdict(lambda: float('inf'))

        while min_heap:
            effort, i, j = heapq.heappop(min_heap)

            if (i, j) == (m-1, n-1):
                return effort
            
            for r, c in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                if 0 <= r < m and 0 <= c < n:
                    new_dist = max(effort, abs(heights[i][j] - heights[r][c]))
                    if new_dist < dist[(r,c)]:
                        dist[(r,c)] = new_dist
                        heapq.heappush(min_heap, (new_dist, r, c)) 


        
        