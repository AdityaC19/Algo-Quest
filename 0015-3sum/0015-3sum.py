class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            seen = set()
            for j in range (i+1, len(nums)):
                complement = -(nums[i] + nums[j])
                if complement in seen:
                    res.add((complement, nums[i], nums[j]))
                seen.add(nums[j])
        
        return [list(i) for i in res]


        