class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = float('-inf')
        res = curSum
        for num in nums:
            curSum = max(num, curSum + num)
            res = max(res, curSum)
        return res