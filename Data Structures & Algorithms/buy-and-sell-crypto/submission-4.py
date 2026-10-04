class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        sell = prices[0]

        for price in prices:
            if price < sell:
                sell = price
            else:
                res = max(res, price - sell)
        
        return res