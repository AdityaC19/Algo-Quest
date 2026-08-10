class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float('inf')
        l = 0
        summ = 0

        for r in range(len(nums)):
            summ += nums[r]

            while summ >= target:
                minLen = min(minLen, r-l+1)
                summ -= nums[l]
                l += 1
                    
        return minLen if minLen < float('inf') else 0
        