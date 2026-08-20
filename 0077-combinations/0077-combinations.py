class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol = []
        ans = []
        
        def backtrack(i):
            if len(sol) == k:
                ans.append(sol[:])
                return
            
            for x in range(i, n+1):
                sol.append(x)
                backtrack(x+1)
                sol.pop()
        
        backtrack(1)
        return ans
                

        