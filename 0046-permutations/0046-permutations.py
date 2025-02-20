class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        n = len(nums)

        def backtracking(i):
            if i == n:
                return res.append(sol.copy())

            for num in nums:
                if num not in sol:
                    sol.append(num)
                    backtracking(i+1)
                    sol.pop()
        
        backtracking(0)
        return res
        