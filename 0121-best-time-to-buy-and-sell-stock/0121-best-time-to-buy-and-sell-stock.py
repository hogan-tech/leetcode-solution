class Solution(object):
    def maxProfit(self, prices):
        smallest_price = 9999
        profit = 0
        for price in prices:
            if price < smallest_price:
                smallest_price = price
            if price - smallest_price > profit:
                profit = price - smallest_price
        return profit