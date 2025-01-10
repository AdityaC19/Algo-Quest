class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i]+nums[j]==target):
                    return [i,j]





















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
                
            
        
