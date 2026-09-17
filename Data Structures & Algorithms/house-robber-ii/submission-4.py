class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
    

        def rob2(nums):
            rob1, rob2 = 0, 0

            for num in nums:
                temp = rob2
                rob2 = max(num + rob1, rob2)
                rob1 = temp
            
            return rob2

        return max(rob2(nums[1:]), rob2(nums[:-1]))