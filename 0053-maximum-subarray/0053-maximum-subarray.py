class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_summ = 0
        max_summ = float('-inf')

        for i in range(len(nums)):
            curr_summ += nums[i]
            if curr_summ > max_summ:
                max_summ = curr_summ
            if curr_summ < 0:
                curr_summ = 0
        
        return max_summ

        