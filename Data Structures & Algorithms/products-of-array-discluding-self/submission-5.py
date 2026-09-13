class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # build a prefix and suffix array
        # since nums[i] = product of prefix and suffix

        # 1, 1, 2, 8
        # arr[i] = arr[i - 1] * nums[i - 1]
        # 48, 24, 6 1
        # arr[i] = arr[i + 1] * nums[i + 1]

        # 1, 0
        # 0, 1

        # res[i] = pre[i] * suf[i]

        pre = [1] * len(nums)
        suf = [1] * len(nums)
        res = [0] * len(nums)

        for i in range(1, len(pre)):
            pre[i] = pre[i - 1] * nums[i - 1]
        
        for i in range(len(suf) - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]
        
        for i in range(len(nums)):
            res[i] = pre[i] * suf[i]
        
        return res