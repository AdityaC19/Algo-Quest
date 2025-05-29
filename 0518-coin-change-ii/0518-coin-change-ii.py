class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(n):
            for a in range(coins[i] , amount +1):
                dp[a] += dp[a - coins[i]]
        return dp[amount]
