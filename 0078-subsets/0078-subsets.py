class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []
        res = []

        def backtrack(i):
            if i == len(nums):
                res.append(sol[:])
                return
            
            backtrack(i+1)

            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        
        backtrack(0)
        return res



        