class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        maxProfit = 0

        for i in prices:
            if i < minimum:
                minimum = i
            diff = i - minimum
            if diff > maxProfit:
                maxProfit = diff
        
        return maxProfit

