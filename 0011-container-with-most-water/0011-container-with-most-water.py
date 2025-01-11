class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        ans = 0
    
        while l < r:
            #diff = abs(height[l] - height[r])
            lo = min(height[l],height[r])
            area = lo * (r-l)
            if area > ans:
                ans = area
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        
        return ans

            

        
        