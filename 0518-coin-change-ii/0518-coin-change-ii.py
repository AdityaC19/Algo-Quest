class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = []
        ans = []

        @cache
        def dfs(i, curSum):
            if curSum > amount or i == len(coins):
                return 0
            
            if curSum == amount:
                return 1 
            
            take = dfs(i, curSum + coins[i])
            skip = dfs(i+1, curSum)
            return take + skip
        
        return dfs(0, 0)


        