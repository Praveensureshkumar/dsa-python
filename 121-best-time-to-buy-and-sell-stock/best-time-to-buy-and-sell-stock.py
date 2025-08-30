class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stock_buy=0
        max_profit=0
        for sell in range(1,len(prices)):
            if prices[sell]<prices[stock_buy]:
                stock_buy=sell
            if prices[sell]>prices[stock_buy]:
                profit=prices[sell]-prices[stock_buy]
                max_profit=max(profit,max_profit)
        return max_profit
        
                