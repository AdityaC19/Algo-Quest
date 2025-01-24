class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        sol = []

        #i=1
        def backtrack(i):
            if len(sol) == k:
                res.append(sol[:])
                return

            if i > n:
                return

            backtrack(i+1)

            sol.append(i)
            backtrack(i+1)
            sol.pop()
            
        backtrack(1)
        return res




