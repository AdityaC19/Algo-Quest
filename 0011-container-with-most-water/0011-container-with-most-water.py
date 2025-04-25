class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        max_area = float('-inf')

        while l < r:
            mini = min(height[l], height[r])
            area = mini * (r-l)
            if area > max_area:
                max_area = area
            if height[l] < height[r]:    
                l += 1
            else:
                r -= 1
        
        return max_area


        