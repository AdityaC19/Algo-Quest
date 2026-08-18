class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n-1]


        # memo = {1:1 ,2: 2}

        # def f(i):
        #     if i in memo:
        #         return memo[i]
        #     else:
        #         memo[i] = f(i-1) + f(i-2)
        #         return memo[i]
        
        # return f(n)




        