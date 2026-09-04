class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # iterate through prices
        # check if price[i] is min:
        # min = price[i]
        # else: price[i] > min
        # so we check profit and store

        profit = 0
        mn = prices[0]
        for price in prices:
            if price < mn:
                mn = price
            else:
                profit = max(profit, price - mn)
        
        return profit