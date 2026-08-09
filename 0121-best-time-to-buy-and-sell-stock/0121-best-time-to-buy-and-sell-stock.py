class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minCost = prices[0]

        for i in range(len(prices)):
            profit = prices[i] - minCost
            if maxProfit > profit:
                minCost = min(minCost, prices[i])
            maxProfit = max(maxProfit, profit)

            #print(maxProfit, minCost)

        return maxProfit 
        