class Solution:
    def rob(self, nums: List[int]) -> int:
        # max profit = nums[i + 1] or nums[i + 2]
        # bottom up: max profit = nums[i - 2] or nums[i - 1]
        memo = [-1] * len(nums)
        def dfs(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            
            skip = dfs(i + 1)
            rob = nums[i] + dfs(i + 2)

            memo[i] = max(skip, rob)
            return memo[i]
        
        return dfs(0)

