class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(cur, total, i):
            if total == target:
                res.append(cur.copy())
            
            for j in range(i, len(nums)):
                if total + nums[j] <= target:
                    cur.append(nums[j])
                    dfs(cur, total + nums[j], j)
                    cur.pop()
                else:
                    break
        
        dfs([], 0, 0)
        return res