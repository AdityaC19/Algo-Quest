class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = float('-inf')
        lowest = prices[0]

        for price in prices:
            if price < lowest:
                lowest = price
            diff = price - lowest
            #print(diff, maxP)
            if diff > maxP:
                maxP = diff
        
        if maxP > 0:
            return maxP
        else:
            return 0

        