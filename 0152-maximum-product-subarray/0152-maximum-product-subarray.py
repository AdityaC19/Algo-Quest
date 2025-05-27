class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        curMax = 1
        curMin = 1

        for n in nums:
            if n == 0:
                curMax, curMin = 1, 1
            
            temp = curMax * n
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(curMin * n, temp, n)
            res = max(curMax, res)
        
        return res

        
        