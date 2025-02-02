import heapq
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        min_heap = [(grid[0][0],0,0)]
        min_path = 0
        seen = defaultdict(lambda: float('inf'))
        seen[(0, 0)] = grid[0][0]

        while min_heap:
            summ, i, j = heapq.heappop(min_heap)
            
            if (i, j) == (m-1, n-1):
                return summ

            for r, c in [(i+1, j), (i, j+1)]:
                if 0 <= r < m and 0 <= c < n:
                    min_path = summ + grid[r][c]
                    if min_path < seen[(r,c)]:
                        seen[(r,c)] = min_path
                        heapq.heappush(min_heap, (min_path, r, c))

        
        print(seen)


        