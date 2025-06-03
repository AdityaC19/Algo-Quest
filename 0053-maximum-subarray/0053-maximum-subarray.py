class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_summ = 0
        max_summ = float('-inf')

        for i in range(len(nums)):
            curr_summ = max(curr_summ, 0)
            curr_summ += nums[i]
            max_summ = max(max_summ, curr_summ)
        
        return max_summ

        