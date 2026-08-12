class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l =0 
        r = len(nums) - 1
        n = len(nums)

        while l < r:
            m = l + (r-l)//2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
            
        min_i = l

        if min_i == 0:
            l, r = 0, n-1
        elif target >= nums[0] and target <= nums[min_i-1]:
            l, r = 0, min_i - 1
        else:
            l, r = min_i, n - 1
        
        while l <= r:
            m = l + (r-l)//2

            if nums[m] == target:
                return m 
            elif nums[m] > target:
                r = m -1
            else:
                l = m + 1
        
        return -1



        
    