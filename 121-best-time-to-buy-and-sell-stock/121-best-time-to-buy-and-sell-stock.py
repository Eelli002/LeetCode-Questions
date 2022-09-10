class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = sell = max_profit = 0
        
        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
            elif prices[sell] - prices[buy] > max_profit:
                max_profit = prices[sell] - prices[buy]
            sell += 1
            
        return max_profit