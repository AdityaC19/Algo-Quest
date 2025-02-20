from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        m, n = len(grid), len(grid[0])
        fresh_oranges = 0
        time = 0

        seen = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh_oranges += 1

        if fresh_oranges == 0:
            return 0
        
        while q:
            time += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for r, c in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                        grid[r][c] = 2
                        #print(grid[r][c])
                        print(fresh_oranges)
                        fresh_oranges -= 1

                        if fresh_oranges == 0:
                            return time
                        
                        seen.add((r,c))
                        q.append((r,c))
                    
        return -1
                
                


                
        