class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}

        @cache
        def dfs(i):
            if i >= n:
                return False
            
            if i == n-1:
                return True
            
            for x in range(1,nums[i]+1):
                if dfs(i+x):
                    return True
            
            return False
        
        return dfs(0)



        