class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            res = nums[abs(num) - 1]
            if res < 0:
                return abs(num)
            else:
                nums[abs(num) - 1] *= -1