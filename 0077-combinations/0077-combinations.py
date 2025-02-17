class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        sol = []

        def backtracking(i):
            if len(sol) == k:
                return res.append(sol[:])

            for x in range(i,n+1):
                sol.append(x)
                backtracking(x+1)
                sol.pop()
                    
        backtracking(1)
        return res




            
            
