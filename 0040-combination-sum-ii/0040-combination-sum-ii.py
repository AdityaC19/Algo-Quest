class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []
        n = len(candidates)
        candidates.sort()

        def backtrack(i, curSum):
            if curSum == target:
                res.append(sol[:])
                return
            
            if i >= n or curSum > target:
                return
            
            sol.append(candidates[i])
            backtrack(i+1, curSum + candidates[i]) 
            sol.pop()
            
            while i+1 < n and candidates[i] == candidates[i+1] :
                i += 1
            backtrack(i+1, curSum)
        
        backtrack(0,0)
        return res

