class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        # 2 3 4 5
        for n in nums:  
            if n - 1 not in nums:
                l = n
                while l + 1 in nums:
                    l += 1
                res = max(res, l - n + 1)
            
        return res