class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Do a binary search to find the minimum value
        so we know the minimum and maximum and their indices

        Do another binary search to find the target based on those two values
        '''

        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        rot = l # this will be the minimum
        # to find index 0, 0 + rot % len(nums) = 4
        # to find index 1, 1 + 4 % 6 = 5
        # to find index 2, 2 + 4 % 6 = 0
        # to find index 3, 3 + 4 % 6 = 1
        # to find index 4, 4 + 4 % 6 = 2
        # to find index 5, 5 + 4 % 6 = 3
        l, r = 0, len(nums) - 1
        n = len(nums)
        while l <= r:
            m = l + (r - l) // 2
            if nums[(m + rot) % n] < target:
                l = m + 1
            elif nums[(m + rot) % n] > target:
                r = m - 1
            else:
                return (m + rot) % n
        return -1