class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum = max(curr_sum, 0)
            curr_sum += nums[i]
            maxSum = max(maxSum, curr_sum)
        
        return maxSum


        