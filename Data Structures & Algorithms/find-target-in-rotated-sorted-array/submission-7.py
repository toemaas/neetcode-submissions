class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 4 6
        # 6 1 2 3 4 5 
        # 5 6 1 2 3 4
        # 3 4 5 6 1 2
        # 1 2 3 4 5 6
        # check if l > m 
            # if target > l or target < m: search left
            # elif target < l and target > m: search right
            # else: target found
        # else l < m
            # if target > l and target < m: search left
            # elif target < l or target > m: search right
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1