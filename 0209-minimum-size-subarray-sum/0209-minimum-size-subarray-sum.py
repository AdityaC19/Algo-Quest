class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        minLen = float('inf')
        ans = []
        cur_sum = 0

        for r in range(len(nums)):
            cur_sum += nums[r]

            while cur_sum >= target:
                if (r-l+1) < minLen:
                    ans = nums[l:r+1]
                    minLen = min(minLen, (r-l+1))
                cur_sum -= nums[l]
                l += 1
                

        return minLen if minLen < float('inf') else 0
            
            
            


        