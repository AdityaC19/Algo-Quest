class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        sol = []

        def backtrack(i):
            if len(sol) == k:
                res.append(sol[:])
                return
            
            #backtrack(i+1)

            for x in range(i, n+1):
                sol.append(x)
                backtrack(x+1)
                sol.pop()

        backtrack(1)
        return res
        