class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        length = 0
        max_length = 0

        # for i in range(n):
        #     if nums[i] == 1:
        #         length += 1
        #         max_length = max(max_length, length)
        #     else: 
        #         length = 0

        l = 0
        
        for r in range(n):
            if nums[r]==0:
                l = r + 1
            w = r - l + 1
            max_length = max(max_length, w)
                
            
        return max_length
        