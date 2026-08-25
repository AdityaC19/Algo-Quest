class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []

        n = len(candidates)

        def backtrack(i, curSum):
            if curSum == target:
                res.append(sol[:])
                return
            
            if curSum > target:
                return
            
            for x in range(i, n):
                sol.append(candidates[x])
                backtrack(x, curSum + candidates[x])
                sol.pop()
        
        backtrack(0, 0)
        return res
        