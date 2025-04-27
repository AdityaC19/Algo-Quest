class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        maxP = float('-inf')

        for price in prices:
            if price < lowest:
                lowest = price
            diff = price - lowest
            if diff > maxP:
                maxP = diff
        
        if maxP > 0:
            return maxP
        else:
            return 0
        