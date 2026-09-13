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
        res = [1] * len(nums)
        prod = 1
        for i in range(1, len(res)):
            res[i] = res[i - 1] * nums[i - 1]
        
        for i in range(len(res) - 1, -1, -1):
            res[i] = res[i] * prod
            prod *= nums[i]
        
        return res