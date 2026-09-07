class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # -4, -1, -1, -1, 0, 1, 2, 3
        nums.sort()

        res = []
        for i in range(len(nums)):
            one = nums[i]

            if i > 0 and one == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                if one + nums[l] + nums[r] > 0:
                    r -= 1
                elif one + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([one, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1
        
        return res