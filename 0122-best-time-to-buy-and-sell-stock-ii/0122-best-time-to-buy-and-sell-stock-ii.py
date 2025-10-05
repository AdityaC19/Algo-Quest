class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        
        return profit
        



        # min_price = prices[0]
        # max_profit = 0
        # n = len(prices)
        # ans = []

        # buy, sell = 0, 0

        # for i in range(n):
        #     min_price = min(min_price, prices[i])
        #     max_profit = max(max_profit, prices[i] - min_price)
        #     ans.append(max_profit)
        #     if max_profit > 0:
        #         min_price = prices[i]
        #         max_profit = 0
        # #print(ans)
        # summ = 0
        # for i in ans:
        #     if i > 0:
        #         summ += i
        # return summ
        

        