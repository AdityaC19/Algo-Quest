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

        # graph = defaultdict(list)

        # for i in range(m):
        #     for j in range(n):
        #         for r,c in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
        #             if 0 <= r < m and 0 <= c < n:
        #                 graph[(i,j)].append((r, c, abs(heights[i][j] - heights[r][c])))
        
        


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
        
        for key, value in seen.items():
            print(key, value) 
        
        return max_diff


        # while q:
        #     for _ in range(len(q)):
        #         i, j = q.popleft()
        #         max_diff = max(max_diff, diff)

        #         if (i, j) == (n - 1, n - 1):
        #             return max_diff

        #         for r, c in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
        #             if 0 <= r < m and 0 <= c < n:
        #                 diff = abs(heights[r][c] - heights[i][j])
        #                 if diff < seen[(r, c)]:  
        #                     q.append((r, c))
        #                     seen[(r, c)] = diff
                        
        
        return max_diff

                
