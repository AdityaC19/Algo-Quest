class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        prefix = 1
        for i in range(n):
            ans[i] *= prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(n-1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]
        
        return ans
        



        # n = len(nums)
        # ans = [0]*n
        # pre = [1]*n
        # post = [1]*n


        # for i in range(1,n):
        #     pre[i] = pre[i-1] * nums[i-1]   # [1 1 2 6]
        
        # for i in range(n-2, -1, -1):
        #     post[i] = post[i+1] * nums[i+1] # [24  12  4 1]
        
        # for i in range(n):
        #     ans[i] = pre[i] * post[i]
        
        # return ans
        