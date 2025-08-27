class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stock_buy=0
        stock_sell=1
        result=0
        while stock_sell<len(prices):
            if prices[stock_sell]>prices[stock_buy]:
                profit=prices[stock_sell]-prices[stock_buy]
                result=max(result,profit)
            else:
                stock_buy=stock_sell
            stock_sell+=1
        return result
        