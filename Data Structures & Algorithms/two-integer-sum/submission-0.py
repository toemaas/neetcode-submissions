class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}

        for i, num in enumerate(nums):
            y = target - num
            if y not in table:
                table[num] = i
            else:
                return [table[y], i]
