class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float('inf')] * (n+1) for _ in range(m+1)]

        dp[m][n-1] = 1
        dp[m-1][n] = 1

        # def closer_to_zero(a,b):
        #     #if abs(a) == abs
        #     return a if abs(a) < abs(b) else b

        # for i in range(1, m):
        #     dp[i][0] = max(1, dp[i-1] - dungeon[i][j])
        #     #dp[i][0] = dp[i+1][0] + dungeon[i][0]
        
        # for i in range(1, n):
        #     dp[0][i] = dp[0][i-1] + dungeon[0][i]
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                min_health = min(dp[i+1][j] - dungeon[i][j], dp[i][j+1]- dungeon[i][j])
                dp[i][j] = max(1, min_health)

                #dp[i][j] = closer_to_zero(dp[i-1][j] + dungeon[i][j], dp[i][j-1] + dungeon[i][j])
                #dp[i][j] = min(abs(dp[i-1][j] + dungeon[i][j]), abs(dp[i][j-1] + dungeon[i][j]))
        
        #print(dp)
        return dp[0][0]
       
        
        
        
        
        