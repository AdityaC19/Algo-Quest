class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
       
        dp = [[1] * n for _ in range(m)]
        
        # Initialize first row and first column to 1
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] =  dp[i][j-1] + dp[i-1][j]
        #print(dp)
        
        return dp[m-1][n-1]
            
        

        