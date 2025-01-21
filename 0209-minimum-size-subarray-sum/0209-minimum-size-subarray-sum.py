class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        min_w = float('inf')
        summ = 0

        for r in range(n):
            summ += nums[r]
            while summ >= target:
                w = r - l + 1
                min_w = min(min_w, w)
                summ -= nums[l]
                l += 1

        return min_w if min_w < float('inf') else 0
                            
        




        