class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 2 2 
        # if stack and top of stack == same number:
        # move to next candidate
        # while stack and stack != same number:
        # pop
        # if total > target:
        # pop
        # elif total == target:
        # move candidate
        # else: push 
        # 3 3 5 5
        # 4 4 4 4
        res = []

        def dfs(i, cur, total):
            if total > target or i >= len(nums):
                return
            elif total == target:
                res.append(cur.copy())
                return
            else:
                cur.append(nums[i])
                dfs(i, cur, total + nums[i])
                cur.pop()
                dfs(i + 1, cur, total)
                    
        dfs(0, [], 0)
        return res