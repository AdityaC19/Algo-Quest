class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []
        n = len(candidates)

        def backtrack(i, curSum):
            if i >= n or curSum > target:
                return
            
            if curSum == target:
                res.append(sol[:])
                return
            
            backtrack(i+1, curSum)

            if curSum < target:
                curSum += candidates[i]
                sol.append(candidates[i])
                backtrack(i, curSum)
                sol.pop()
        
        backtrack(0,0)
        return res