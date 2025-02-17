class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sol = []
        
        def backtracking(i):
            # index out of bounds condition
            if i == len(nums):
                return ans.append(sol[:])
            
            # dont pick 
            backtracking(i+1)

            # pick condition
            sol.append(nums[i])
            backtracking(i+1)
            
            #backtracking part
            sol.pop()
        
        backtracking(0)
        return ans
            

            



