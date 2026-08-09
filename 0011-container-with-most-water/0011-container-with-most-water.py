class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxarea = 0

        for i in range(len(height)):
            area = (r-l) * min(height[l], height[r])
            #print(area, l, r)
            maxarea = max(maxarea, area)

            if height[l] < height[r]:
                l += 1
            else: 
                r -= 1
        
        return maxarea

        