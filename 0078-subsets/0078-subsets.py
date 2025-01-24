class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        sol = []

        def backtracking(i):
            if i == n:
                return res.append(sol[:])
            
            #Dont pick nums[i] --> left nodes
            backtracking(i+1)

            #To pick nums[i] --> right nodes
            sol.append(nums[i])
            backtracking(i+1)
            sol.pop()

        
        backtracking(0)
        return res
