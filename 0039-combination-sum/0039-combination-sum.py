class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        sol = []

        def backtracking(i, curSum):
            if i >= n or curSum > target:
                return 

            if curSum == target:
                return res.append(sol.copy())

            backtracking(i+1, curSum)

            if curSum < target:
                curSum += candidates[i]
                sol.append(candidates[i])
                backtracking(i, curSum)
                sol.pop()
            
        backtracking(0,0)
        return res


