class Solution:
    def rob(self, nums: List[int]) -> int:
        def houseRobber(nums):
            n = len(nums)

            # if n == 1: return nums[0]
            # if n == 2: return max(nums[0], nums[1])

            dp = [0] * n

            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, n):
                dp[i] = max(dp[i-2]+nums[i], dp[i-1])
            
            return dp[n-1]

        n = len(nums)

        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])
        
        return max(houseRobber(nums[:-1]), houseRobber(nums[1:]))
        