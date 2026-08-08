class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n
        post = [1] * n

        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = pre[i-1] * nums[i]

        post[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            post[i] = post[i+1] * nums[i]
        
        #print(pre)
        #print(post)

        ans = [1] * n
        for i in range(n):
            left = pre[i-1] if i > 0 else 1
            right = post[i+1] if i < n-1 else 1
            ans[i] = left * right
        
        return ans