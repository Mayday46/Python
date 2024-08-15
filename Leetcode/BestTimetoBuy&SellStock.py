'''
121. Best Time to Buy and Sell Stock

You are given an array prices where price4s[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0

Example 1:
    Input: prices = [7, 1, 5, 3, 6, 4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5
    Note: Buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


Exmaple 2:
    Input: prices = [7, 6, 4, 3, 1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.


UIP

Understand:
    - Cannot travel back in time.
    - Once you buy, you can only move forward.
'''
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy, sell = 0, 1
        maxProfit = 0

        while sell < len(prices):
            if prices[buy] > prices[sell]:
                # If current buy day is more expensive than sell day, move buy day to sell day
                buy = sell
            else:
                # Calculate profit and update maxProfit if this profit is higher
                currentProfit = prices[sell] - prices[buy]
                maxProfit = max(maxProfit, currentProfit)
            
            # Move the sell day forward
            sell += 1
        
        return maxProfit
