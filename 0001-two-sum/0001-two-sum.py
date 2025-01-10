class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i in range(len(nums)):
            x = target - nums[i]
            if x in hmap:
                return [i, hmap[x]]
            hmap[nums[i]] = i




















        '''
        map = {}
        n = len(nums)

        for i in range(n):
            x = target - nums[i]
            if x in map:
                return [map[x], i]
            map[nums[i]] = i
        
        return []
        '''
                
            
        
