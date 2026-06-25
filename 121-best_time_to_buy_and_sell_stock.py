"""
121. Best Time to Buy and Sell Stock
Attempted
Easy
Topics
conpanies icon
Companies
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
 
"""

#time: O(n^2)
#space: O(n)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = float('-inf')
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                profit = max(profit, prices[j] - prices[i])
        return 0 if profit <= 0 else profit

#time: O(n)
#space: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = float("inf")
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            profit = prices[i] - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit
 
