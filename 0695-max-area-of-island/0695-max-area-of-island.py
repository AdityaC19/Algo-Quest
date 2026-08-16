class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        area = 0

        def dfs(i, j):
            nonlocal area
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return 
            
            grid[i][j] = '#'
            area += 1

            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)
        
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = 0
                    dfs(i, j)
                maxArea = max(maxArea, area)

        return maxArea
        