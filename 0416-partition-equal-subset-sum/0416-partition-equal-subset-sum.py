class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        ans = []

        total = sum(nums)

        if total % 2 != 0:
            return False
        
        target = total // 2

        @cache
        def dfs(i, curSum):
            if curSum > target or i >= len(nums):
                return False
            
            if curSum == target:
                return True
            
            return dfs(i+1, curSum + nums[i]) or dfs(i+1, curSum)
        
        return dfs(0,0)




        