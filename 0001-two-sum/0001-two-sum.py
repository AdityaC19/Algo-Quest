class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        n = len(nums)
        ans = []

        for i in range(n):
            x = target - nums[i]
            if x in hmap:
                return [i, hmap[x]]
            else:
                hmap[nums[i]] = i
        
    