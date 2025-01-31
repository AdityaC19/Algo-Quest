from collections import deque
import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m,n = len(heights), len(heights[0])
        q = deque()
        q.append((0,0))
        seen = defaultdict(lambda: float('inf'))
        diff = 0
        max_diff = 0


        min_heap = [(0,0,0)] # (effort, i, j)

        while min_heap:
            diff, i, j = heapq.heappop(min_heap)
            max_diff = max(max_diff, diff)

            if (i,j) == (m-1, n-1):
                break
            
            for r,c in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                if 0 <= r < m and 0 <= c < n:
                    new_diff = max(diff, abs(heights[r][c] - heights[i][j]))
                    if new_diff < seen[(r, c)]:  
                        heapq.heappush(min_heap, (new_diff, r,c))
                        seen[(r, c)] = new_diff
        
        return max_diff


                
