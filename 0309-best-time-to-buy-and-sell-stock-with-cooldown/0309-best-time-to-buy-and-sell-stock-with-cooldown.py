class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        #dp = {}     # key=(i, buying) val=max_profit

        dp = [[0, 0] for _ in range(n+2)]
        maxProfit = 0

        for i in range(n-1, -1, -1):
            # buying j = 1
            dp[i][1] = max(dp[i+1][0] - prices[i], dp[i+1][1])
            # selling j = 0
            dp[i][0] = max(dp[i+2][1] + prices[i], dp[i+1][0])
        
        return dp[0][1] # start with the ability to buy






        # def dfs(i, buying): # (i, bool)
        #     if i >= n:
        #         return 0
            
        #     if (i, buying) in dp:
        #         return dp[(i, buying)]
            
        #     if buying:
        #         buy = dfs(i+1, not buying) - prices[i]
        #         cooldown = dfs(i+1, buying)
        #         dp[(i, buying)] = max(buy, cooldown)
        #     else:
        #         sell = dfs(i+2, not buying) + prices[i]
        #         cooldown = dfs(i+1, buying)
        #         dp[(i, buying)] = max(sell, cooldown)
        #     return dp[(i, buying)]
        
        # return dfs(0, True)




        