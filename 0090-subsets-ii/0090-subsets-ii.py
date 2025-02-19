class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        sol = []

        nums.sort()

        def backtracking(i):
            if i == len(nums):
                return res.append(sol[:])

            sol.append(nums[i]) 
            backtracking(i+1)
            sol.pop()

            while i+1 < n and nums[i] == nums[i+1]:
                i += 1

            backtracking(i+1)

        
        backtracking(0)
        return res