class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        
        dp = [[1] * n for _ in range(m)]

        dp[0][1] = 1
        dp[1][0] = 1

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] =  dp[i][j-1] + dp[i-1][j]
        print(dp)
        
        return dp[m-1][n-1]
            
        

        