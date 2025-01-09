class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = float('inf')
        maxP = 0

        for price in prices:
            if price < minimum:
                minimum = price
            diff = price - minimum
            if diff > maxP:
                maxP = diff
        
        return maxP
        
           
        