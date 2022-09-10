class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        end = 0
        max_profit = 0
        
        while end < len(prices):
            if prices[start] > prices[end]:
                start = end
            elif prices[end] - prices[start] > max_profit:
                max_profit = prices[end] - prices[start]
            end += 1
            
        return max_profit