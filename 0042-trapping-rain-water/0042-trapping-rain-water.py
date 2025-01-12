class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l,r = 0, n-1
        maxLeftHeight = height[l]
        maxRightHeight = height[r]

        total = 0

        while l < r:
            if maxLeftHeight < maxRightHeight:
                l += 1
                maxLeftHeight = max(maxLeftHeight, height[l])
                total += maxLeftHeight - height[l]
            else:
                r -= 1
                maxRightHeight = max(maxRightHeight, height[r])
                total += maxRightHeight - height[r]
        
        return total






        