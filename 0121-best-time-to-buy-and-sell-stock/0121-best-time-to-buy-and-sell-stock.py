class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        lowest = prices[0]
        maxP = 0
        
        for i in range(n):
            if prices[i] < lowest:
                lowest = prices[i]
            diff = prices[i] - lowest
            if diff > maxP:
                maxP = diff
        
        return maxP
