class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}

        def dfs(i, curSum):
            if i == n:
                return 1 if curSum == target else 0
            
            if (i, curSum) in memo:
                return memo[(i, curSum)]

            add = dfs(i + 1, curSum + nums[i])
            sub = dfs(i + 1, curSum - nums[i])

            result = add + sub
            memo[(i, curSum)] = result
            return result
            
        
        return dfs(0,0)
