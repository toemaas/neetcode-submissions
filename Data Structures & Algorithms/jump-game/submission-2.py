class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxLen = 0
        for i, num in enumerate(nums):
            if maxLen >= len(nums) - 1:
                return True
            maxLen = max(maxLen, i + num)
            if maxLen == i and num == 0:
                return False
        return False