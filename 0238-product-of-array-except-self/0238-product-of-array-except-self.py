class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        #pre = [1] * n
        #post = [1] * n
        ans = [1] * n

        prefix = 1
        suffix = 1

        for i in range(n):
            ans[i] *= prefix
            prefix *= nums[i]
        
        for i in range(n-1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]
        
        return ans

        # for i in range(1, n):
        #     pre[i] = pre[i-1] * nums[i-1]
        
        # for i in range(n-2, -1, -1):
        #     post[i] = post[i+1] * nums[i+1]
        
        # for i in range(n):
        #     ans[i] = pre[i] * post[i]
        
        # return ans
        

        # for i in range(n):
        #     prod = 1
        #     for j in range(n):
        #         if (i == j): continue
        #         prod *= nums[j]
        #     ans[i] = prod
        
        # return ans
        