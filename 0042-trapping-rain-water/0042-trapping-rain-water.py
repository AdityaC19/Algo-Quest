class Solution:
    def trap(self, height: List[int]) -> int:
        l_wall = r_wall = 0
        n = len(height)
        maxLeftHeight = [0] * n 
        maxRightHeight = [0] * n

        for i in range(n):
            j = -i-1
            maxLeftHeight[i] = l_wall
            maxRightHeight[j] = r_wall
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])
        
        total = 0
        for i in range(n):
            water = min(maxLeftHeight[i], maxRightHeight[i])
            total += max(0, water-height[i])

        return total



        