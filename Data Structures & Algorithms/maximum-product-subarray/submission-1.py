class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = 1
        minProd = 1
        res = float('-inf')
        for n in nums:
            temp = maxProd * n
            maxProd = max(maxProd * n, n, minProd * n)
            minProd = min(minProd * n, n, temp)
            res = max(res, max(maxProd, minProd))
        # 2, 4
        # 2, 4
        # max of 2* 4 or 4
        # 2, 4, -3 
        # 
        return res