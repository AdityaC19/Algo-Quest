class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        ans = []

        i = 0
        while i < n:
            temp = nums[i]
            while i+1 < n and nums[i+1] == nums[i]+1:
                i += 1
            
            if nums[i] == temp:
                ans.append(str(temp))
            else:
                ans.append(str(temp) + "->" + str(nums[i]))
            i+=1        
        return ans


        