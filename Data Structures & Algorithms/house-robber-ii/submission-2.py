class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]

        def robb(arr):
            if len(arr) < 2:
                return arr[0]
            dp = [-1] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                dp[i] = max(arr[i] + dp[i - 2], dp[i - 1])

            return dp[-1]
        
        return max(robb(nums[1:]), robb(nums[:-1]))