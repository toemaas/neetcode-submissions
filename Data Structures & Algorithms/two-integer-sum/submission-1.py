class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums[i] + nums[j] == target
        # X + nums[j] == target
        # target - nums[i] == nums[j]
        # 7 - 3 = 4
        # 7 - 4 = 3

        m = {}

        for idx, num in enumerate(nums):
            j = target - num
            if j in m:
                return [m[j], idx]
            m[num] = idx