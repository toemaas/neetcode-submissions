class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = minProd = 1
        res = nums[0]
        # negative val * negative num = pos
        # negative val * pos num = neg

        # pos val * negative num = neg
        # pos val * pos num  = pos

        for num in nums:
            temp = maxProd
            maxProd = max(maxProd * num, num, minProd * num)
            minProd = min(minProd * num, num, temp * num)
            res = max(res, maxProd)

        return res
