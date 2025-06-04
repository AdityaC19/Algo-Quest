class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        minLen = float('inf')
        summ = 0

        for r in range(len(nums)):
            summ += nums[r]
            while summ >= target:
                w = r-l+1
                minLen = min(minLen, w)
                summ -= nums[l]
                l += 1
        
        return minLen if minLen < float('inf') else 0
        


        