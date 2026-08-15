class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        maxl = (height[l])
        maxh = (height[r])
        ans = 0

        while l < r:
            if height[l] < height[r]:
                maxl = max(maxl, height[l])
                ans += maxl - height[l]
                l += 1
            else:
                maxh = max(maxh, height[r])
                ans += maxh - height[r]
                r -= 1
        
        return ans


                

        