class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        sol = []

        nums.sort()

        def backtracking(i):
            if i == len(nums):
                return res.add(tuple(sol[:]))
            
            backtracking(i+1)

            sol.append(nums[i])
            backtracking(i+1)
            sol.pop()

            
        
        backtracking(0)
        return list(res)