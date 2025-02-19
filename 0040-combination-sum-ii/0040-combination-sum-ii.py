class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        sol = []

        candidates.sort()

        def backtracking(i, curSum):
            if curSum == target:
                return res.append(sol[:])
            
            if i >= n or curSum > target:
                return

            #if curSum < target:
            #curSum += candidates[i]
            sol.append(candidates[i])
            backtracking(i+1, curSum + candidates[i])
            sol.pop()
            
            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1 

            backtracking(i+1, curSum)

        backtracking(0,0)
        return res