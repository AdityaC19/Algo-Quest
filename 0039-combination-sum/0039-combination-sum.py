class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []

        def backtrack(i, sum):


            if sum == target:
                res.append(sol[:])
                return 
            
            if i >= len(candidates) or sum > target:
                return

            sol.append(candidates[i])
            backtrack(i, sum+candidates[i])
            sol.pop()
            backtrack(i+1, sum)

        
        backtrack(0, 0)
        return res

        