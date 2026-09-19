class Solution:
    def numDecodings(self, s: str) -> int:
        """
        input: string of digits
        output: int ways to decode

        plan:

        at each step: can choose either one digit 1-9 or two digits within 10-19 and 20-26
        base case: 0: return 0
        """
        dp = {len(s) : 1}
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if s[i] == "1" and i + 1 < len(s) or (i + 1 < len(s) and s[i] == "2" and s[i + 1] in "0123456"):
                res += dfs(i + 2)
                
            dp[i] = res
            return res

        return dfs(0)

