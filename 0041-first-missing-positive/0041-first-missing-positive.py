class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = max(nums)
        nums = set(nums)

        for i in range(1, n+1):
            if i in nums:
                continue
            else:
                return i
        
        if n < 0:
            return 1
        else:
            return n+1
        



        