class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix, suffix = 1, 1
        res = nums[0]
        n = len(nums)

        for i in range(len(nums)):
            if not prefix: prefix = 1
            if not suffix: suffix = 1

            prefix *= nums[i]
            suffix *= nums[n - i - 1]

            res = max(res, prefix, suffix)
        return res