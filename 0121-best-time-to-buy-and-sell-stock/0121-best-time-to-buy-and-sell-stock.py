class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l = 0
        maxProfit = 0

        for r in range(n):
            #minimum = prices[l]
            if prices[r] < prices[l]:
                l = r
            diff = prices[r] - prices[l]
            maxProfit = max(maxProfit, diff)
        
        return maxProfit
                



        