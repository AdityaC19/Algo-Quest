class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]
        dp[0][0] = 1 # When nums is empty and target is 0, there is only one possible way

        for i in range(len(nums)):
            for curr_sum, count in dp[i].items():
                dp[i+1][curr_sum - nums[i]] += count
                dp[i+1][curr_sum + nums[i]] += count
        
        return dp[len(nums)][target]
        
        # n = len(nums)
        # memo = {}
         
        # def dfs(i, curSum):
        #     if i >= n :
        #         return 1 if curSum == target else 0
            
        #     if (i,curSum) in memo:
        #         return memo[(i,curSum)]
            
        #     add = dfs(i+1, curSum + nums[i])
        #     sub = dfs(i+1, curSum - nums[i])

        #     memo[(i,curSum)] = add + sub
        #     return memo[(i,curSum)]
        
        # return dfs(0,0)

        