class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_count = 0
        l = 0
        zeros = 0

        for r in range(n):
            if nums[r] == 0:
                zeros += 1
            
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            
            w = (r-l) + 1
            max_count = max(max_count, w)



                
        return max_count
            
            
