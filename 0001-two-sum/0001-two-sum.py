class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = defaultdict(int)

        for i in range(len(nums)):
            x = target - nums[i]
            if x in hmap:
                return [hmap[x], i]
            hmap[nums[i]] = i
