class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = {}

        for num in nums:
            if num in hashSet:
                return True
            hashSet[num] = 1
        
        return False