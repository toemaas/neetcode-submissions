class Solution:
    def numDecodings(self, s: str) -> int:
        # ways to decode starting from index 0:
        # take 0 char + double char
        # num ways to decode from index i: = dfs(i + 1) + dfs(i + 2)
        # base cases: i > len(s)
        # caching

        memo = {}

        def dfs(i):
            if i >= len(s):
                return 1
            if s[i] == "0":
                return 0

            if i in memo:
                return memo[i]
            res = 0
            res += dfs(i + 1)

            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                res += dfs(i + 2)
            
            memo[i] = res
            return res
        
        return dfs(0)