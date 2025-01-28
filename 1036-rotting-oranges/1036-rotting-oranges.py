from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        time = 0
        fresh = 0

        q = deque() 

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        
        while q:
            time += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for r, c in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh -= 1
                        print(time, "popped", i,j, "neigh:", r, c, fresh)
                        if fresh == 0:
                            return time

                        q.append((r,c))
    
        return time if fresh == 0 else -1



        # while q:
        #     node = q.popleft()
        #     for nei in node.


        # def dfs(i,j):
        #     nonlocal time

        #     if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
        #         return 

        #     elif grid[i][j] == 1:
        #         pass
                
        #     else:
        #         grid[i][j] == 2

        #         dfs(i+1, j)
        #         dfs(i, j+1)
        #         dfs(i-1, j)
        #         dfs(i, j-1)
            


        # return time