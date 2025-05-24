class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        area = 0
        max_area = 0

        def dfs(i,j):
            nonlocal area
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != 1:
                return 0
            
            grid[i][j] = '#'
            area += 1

            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = 0
                    dfs(i,j)
                max_area = max(max_area, area)
        
        return max_area
        