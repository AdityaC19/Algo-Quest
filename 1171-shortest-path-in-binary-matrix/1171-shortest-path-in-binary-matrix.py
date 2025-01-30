from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        q.append((0,0))
        seen = set()
        dist = 0

        if grid[0][0] != 0 or grid[n-1][n-1]!=0:
            return -1
        
        while q:
            dist+=1
            for _ in range(len(q)):
                i, j = q.popleft()
                if (i, j) == (n-1, n-1):
                    return dist
                for r,c in [(i+1, j), (i-1,j), (i, j+1), (i,j-1), (i+1, j+1), (i-1, j-1), (i+1, j-1), (i-1,j+1)]:
                    if 0 <= r < n and 0 <= c < n and grid[r][c] == 0 and (r,c) not in seen:
                        q.append((r,c))
                        seen.add((r,c))
            

        # for i in range(n):
        #     for j in range(n):
        #         if grid[i][j] == 0:
        #             bfs(i, j)

        
        return -1
            

        