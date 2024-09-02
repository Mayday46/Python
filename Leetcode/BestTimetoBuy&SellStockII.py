class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalProfit = 0
        for current in range(1, len(prices)):
            if prices[current] > prices[current - 1]:
                totalProfit += prices[current] - prices[current - 1]
        
        return totalProfit
