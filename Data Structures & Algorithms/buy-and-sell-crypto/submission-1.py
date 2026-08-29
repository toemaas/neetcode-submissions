class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 7 ... 6
        # 7 8 9 6 60
        # if i < current price:
        #   price = prices[i]
        # elif i > current price:
        #   profit = max(profit, prices[i] - price)
        res = 0
        curr = prices[0]
        for price in prices:
            if price < curr:
                curr = price
            else:
                res = max(res, price - curr)

        return res