class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 0 1 2 3 4 5 6
        nums = set(nums)
        res = 0
        for n in nums:
            if n - 1 not in nums:
                count = 0
                seq = n
                while seq in nums:
                    count += 1
                    seq += 1
                res = max(res, count)
        return res