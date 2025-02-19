class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []

        def backtracking():
            if len(sol) == len(nums):
                return res.append(sol[:])
            
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtracking()
                    sol.pop()
        
        backtracking()
        return res
        