class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        if target < nums[l]:
            return 0
        elif target > nums[r]:
            return n

        while l <= r:
            m = l + ((r-l)//2)

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        if l == m:
            return l
        else:
            return r+1