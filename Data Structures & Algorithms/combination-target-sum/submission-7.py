class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(i, cur, amnt):
            if i >= len(nums):
                return
            
            if amnt == target:
                res.append(cur.copy())
                return

            for j in range(i, len(nums)):
                if amnt + nums[j] > target:
                    return
                if amnt + nums[j] <= target:
                    cur.append(nums[j])
                    dfs(j, cur, amnt + nums[j])
                    cur.pop()
        
        dfs(0, [], 0)
        return res