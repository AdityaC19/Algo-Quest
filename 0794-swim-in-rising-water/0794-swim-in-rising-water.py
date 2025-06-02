class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        min_heap = [(grid[0][0], 0, 0)]     #(time, i, j)
        seen = set()

        res = 0
        
        while min_heap:
            time, i, j = heapq.heappop(min_heap)
            res = max(res, time)

            if (i, j) == (m-1, n-1):
                return res
            
            for r, c in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                if 0 <= r < m and 0 <= c < n and (r,c) not in seen:
                    heapq.heappush(min_heap, (grid[r][c], r, c))
                    seen.add((r,c))
         

        