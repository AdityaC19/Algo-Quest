class Solution:
    def minOperations(self, nums: list[int]) -> int:
        diff = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                diff += (nums[i] - nums[i+1])
        
        return diff
        
        
        

                
        
        


        