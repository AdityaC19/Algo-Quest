class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        maxSum = nums[0]
        cur_sum = 0

        for i in range(n):
            cur_sum = max(cur_sum, 0)
            cur_sum += nums[i]
            maxSum = max(maxSum, cur_sum)

        return maxSum        