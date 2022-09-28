class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = l = r = 0
        
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                max_profit = max(prices[r] - prices[l], max_profit)
                
        return max_profit