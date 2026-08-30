class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = [1] * len(nums)

        # 1 2 4 6
        # 1 1 2 8
        #48 24 6 1

        for i in range(1, len(nums)):
            prefix.append(nums[i - 1] * prefix[-1])
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = nums[i + 1] * postfix[i + 1]

        res = []

        for i in range(len(nums)):
            res.append(prefix[i] * postfix[i])
        
        return res