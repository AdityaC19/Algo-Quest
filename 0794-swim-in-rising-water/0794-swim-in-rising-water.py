class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        min_heap = [(grid[0][0], 0 ,0)]  # (time, i, j)
        seen = set()

        while min_heap:
            time, i, j = heapq.heappop(min_heap)

            if i == n-1 and j == n-1:
                break

            for r, c in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                if 0 <= r < n and 0 <= c < n and (r,c) not in seen:
                    heapq.heappush(min_heap, (max(time, grid[r][c]), r,c))
                    seen.add((r,c))
        
        return time

            



        

        