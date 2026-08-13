class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        # prefix = 1
        # for i in range(n):
        #     ans[i] *= prefix
        #     prefix *= nums[i]
        
        # post = 1
        # for i in range(n-1, -1, -1):
        #     ans[i] *= post
        #     post *= nums[i]
        
        # return ans

        pre = [1]*n
        post = [1]*n

        for i in range(1, n):
            pre[i] = pre[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            post[i] = post[i+1] * nums[i+1]
        
        for i in range(n):
            ans[i] = pre[i] * post[i]
        
        return ans



              