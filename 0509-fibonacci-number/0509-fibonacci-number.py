class Solution:
    def fib(self, n: int) -> int:
        memo = {0:0, 1:1}

        def f(i):
            if i in memo:
                return memo[i]
            else:
                memo[i] = f(i-2) + f(i-1)
                return memo[i]
        
        return f(n)
        
        