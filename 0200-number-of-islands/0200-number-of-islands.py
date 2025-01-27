class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        m, n = len(grid), len(grid[0])

        graph = defaultdict(list)

        def dfs(i, j):
            if i >= m or j >= n or i < 0 or j < 0 or grid[i][j] != '1':
                return 
            
            #char = grid[i][j]
            grid[i][j] = '0'

            return dfs(i+1, j) or dfs(i, j+1) or dfs(i-1, j) or dfs(i, j-1)

        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i, j)
        
        return islands
                    
        




        