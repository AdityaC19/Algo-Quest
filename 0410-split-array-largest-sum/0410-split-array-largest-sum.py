class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def helper(nums, max_sum, k):
            count = 1
            cur_sum = 0
            for num in nums:
                cur_sum += num
                if cur_sum > max_sum:
                    count += 1
                    cur_sum = num
                    if count > k:
                        return False
            return True
        
        l, r = max(nums), sum(nums)
        ans = r

        while l <= r:
            m = l + (r-l)//2
            if helper(nums, m, k):
                ans = m 
                r = m - 1
            else:
                l = m + 1
        
        return ans



        