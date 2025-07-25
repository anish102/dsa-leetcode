"""
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
"""


# Brute force solution with O(n^2) time complexity.
# We iterate through each pair of days and calculate the profit.
# Time complexity: O(n^2)
def maxProfit(prices: list[int]) -> int:
    max_profit = 0
    count = range(len(prices))
    for i in count:
        for j in count[i + 1 :]:
            if prices[j] > prices[i]:
                profit = prices[j] - prices[i]
                max_profit = profit if profit > max_profit else max_profit
    return max_profit


# Optimized solution with O(n) time complexity.
# We keep track of the minimum price seen so far and calculate the profit at each step.
# Time complexity: O(n)
def maxProfitOptimized(prices: list[int]) -> int:
    max_profit = 0
    min_price = max(prices)
    for price in prices:
        min_price = min(price, min_price)
        cur_profit = price - min_price
        max_profit = max(cur_profit, max_profit)
    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
print(maxProfitOptimized(prices))
