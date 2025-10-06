class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = 1
        post = 1
        ans = [1] * n

        for i in range(n):
            ans[i] *= pre
            pre *= nums[i]
        
        for i in range(n-1, -1, -1):
            ans[i] *= post
            post *= nums[i]
        
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
        