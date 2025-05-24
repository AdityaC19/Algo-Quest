class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        islands = 0

        seen = set()

        def bfs(i, j):
            q = deque([(i,j)])

            while q:
                i,j = q.popleft()
                for r, c in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= r < m and 0 <= c < n and (r,c) not in seen and grid[r][c] == '1':
                        q.append((r,c))
                        seen.add((r,c))
        
        for i in range(m):
            for j in range(n):
                if (i,j) not in seen and grid[i][j] == '1':
                    seen.add((i,j))
                    islands += 1
                    bfs(i,j)

        return islands
    


        