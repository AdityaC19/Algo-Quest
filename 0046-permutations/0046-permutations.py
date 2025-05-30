class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol = []
        res = []

        def backtrack(i):
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            
            for x in range(len(nums)):
                if nums[x] not in sol:
                    sol.append(nums[x])
                    backtrack(x+1)
                    sol.pop()
            
        backtrack(0)
        return res

        