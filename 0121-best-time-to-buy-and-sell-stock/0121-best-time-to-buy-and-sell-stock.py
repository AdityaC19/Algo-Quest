class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minCost = prices[0]

        for i in range(len(prices)):
            minCost = min(minCost, prices[i])
            profit = prices[i] - minCost
            maxProfit = max(maxProfit, profit)

        return maxProfit 
        