class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # res = 0
        # curr = prices[0]
        # for price in prices:
        #     if price < curr:
        #         curr = price
        #     else:
        #         res = max(res, price - curr)

        # return res
        l, r = 0, 0
        profit = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                profit = max(profit, prices[r] - prices[l])
            r += 1
        return profit