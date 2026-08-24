class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        lsum = 0
        rsum = total

        for i in range(len(nums)):
            rsum -= nums[i]

            if lsum == rsum:
                return i
            
            lsum += nums[i]
        
        return -1
            
        