class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        idx = 0
        smol = nums[0]

        dp = [1] * n

        # for i in range(n):
        #     if nums[i] < smol:
        #         smol = nums[i]
        #         idx = i
        
        # stk = [smol]
        
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
                    #print(dp)

        return max(dp)





        
        