class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        seen = set()
        area = 0

        def bfs(i, j):
            nonlocal area
            q = deque([(i,j)])

            while q:
                i, j = q.popleft()
                for r, c in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                    if 0 <= r < m and 0 <= c < n and (r,c) not in seen and grid[r][c] ==1:
                        q.append((r,c))
                        seen.add((r,c))
                        area+=1
        
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if (i,j) not in seen and grid[i][j] == 1:
                    seen.add((i,j))
                    area = 1
                    bfs(i, j)
                maxArea = max(maxArea, area)

        return maxArea
        