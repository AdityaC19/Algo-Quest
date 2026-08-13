class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        maxP = 0

        for price in prices:
            lowest = min(lowest, price)
            maxP = max(maxP, price - lowest)
        
        return maxP
        