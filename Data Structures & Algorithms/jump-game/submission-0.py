class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump = nums[0]
        idx = 0
        while idx < len(nums):
            if idx > maxJump:
                return False
            elif maxJump >= len(nums):
                return True
            maxJump = max(maxJump, idx + nums[idx])
            idx += 1
        
        return True