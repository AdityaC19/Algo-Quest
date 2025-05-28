class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        a = float('inf')
        b = float('inf')

        for i in range(n):
            if nums[i] <= a:
                a = nums[i]
            elif nums[i] <= b:
                b = nums[i]
            else:
                return True
        
        return False
            
            
            

            


        # max_w = 0
        # l = 0

        # for r in range(1,n):
        #     if nums[l] >= nums[r]:
        #         l = r
        #     w = r - l + 1
        #     max_w = max(max_w, w)
        
        # return True if max_w >= 3 else False

            
        
        