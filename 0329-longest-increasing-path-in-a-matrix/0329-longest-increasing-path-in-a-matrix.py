class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        @cache
        def dfs(i, j):
            maxlen = 1

            for r, c in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                if 0 <= r < m and 0 <= c < n and matrix[r][c] > matrix[i][j]:
                    maxlen = max(maxlen, 1 + dfs(r,c))
            return maxlen
            
        max_path = 0
        for i in range(m):
            for j in range(n):
                max_path = max(max_path, dfs(i,j))

        return max_path




        