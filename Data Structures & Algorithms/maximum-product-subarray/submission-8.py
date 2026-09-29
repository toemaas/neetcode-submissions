class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # three cases: all positive, one negative, two negative, zero
        # negative numbers can flip, so keep track of max and min
        res = float('-inf')
        curMin = curMax = 1

        for num in nums:
            temp = curMax
            curMax = max(num, num * curMax, num * curMin)
            curMin = min(num, num * temp, num * curMin)
            res = max(res, curMax)
        
        return res