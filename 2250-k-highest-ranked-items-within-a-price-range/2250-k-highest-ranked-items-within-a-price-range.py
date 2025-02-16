from collections import deque
import heapq

class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        dist = 0
        
        x,y = start
        min_heap = [(0, grid[x][y], x, y)]
        seen = set()
        seen.add(tuple(start))
        ans = []

        while min_heap and len(ans) < k:
            dist, value, i, j = heapq.heappop(min_heap)
            if pricing[0] <= value <= pricing[1]:
                ans.append([i,j])
            for r, c in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                if 0 <= r < m and 0 <= c < n and (r,c) not in seen and grid[r][c] != 0:
                    # if pricing[0] <= grid[r][c] <= pricing[1]:
                    #     if len(min_heap) < k:
                    #         heapq.heappush(min_heap, (dist+1, grid[r][c], (r,c)))
                    seen.add((r,c))
                    heapq.heappush(min_heap, (dist+1, grid[r][c], r,c))

        return ans

