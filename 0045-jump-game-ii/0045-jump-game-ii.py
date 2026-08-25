class Solution:
    def jump(self, nums: List[int]) -> int:

        n = len(nums)

        farthest = 0
        target = 0

        jumps = 0

        for i in range(n-1):
            farthest = max(nums[i]+i, farthest)
            if i == target:
                jumps += 1
                target = farthest

        return jumps 

        