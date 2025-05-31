class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dfs(i, j):
            if i == m-1 and j == n-1:
                return 1
            
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            res = 0
            for r, c in [(i+1, j), (i, j+1)]:
                res += dfs(r, c)
            
            memo[(i,j)] = res
            
            return memo[(i,j)]

        return dfs(0,0)
                    
        