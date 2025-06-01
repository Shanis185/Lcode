class Solution(object):
    def maxProfit(self, prices):
        max_profit=0
        min_price=float('inf')
        for i in prices:
            if i<min_price:
                min_price=i
            profit=i-min_price
            if profit>max_profit:
                max_profit=profit
        return max_profit

        