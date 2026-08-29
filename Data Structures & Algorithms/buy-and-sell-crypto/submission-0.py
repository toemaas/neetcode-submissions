class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0
        for idx, price in enumerate(prices):
            if price >= prices[l]:
                res = max(res, price - prices[l])
            else:
                l = idx
        return res