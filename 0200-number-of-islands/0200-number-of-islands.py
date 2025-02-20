class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1':
                return False

            grid[i][j] = '#'
            
            if dfs(i+1, j) or dfs(i, j+1) or dfs(i-1,j) or dfs(i, j-1):
                return True
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i,j)

        return count
                

        