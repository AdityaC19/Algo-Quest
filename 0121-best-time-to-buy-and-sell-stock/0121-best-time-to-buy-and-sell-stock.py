class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxP = 0

        for r in range(len(prices)):
            while prices[r] < prices[l] and r < len(prices):
                l = r
            w = (prices[r]-prices[l]) 
            maxP = max(maxP, w)
        
        return maxP
        


        