class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        memo = [-1] * len(s)

        def dfs(i):
            if i >= len(s):
                return 1
            if s[i] == "0":
                return 0
            if memo[i] != -1:
                return memo[i]
            
            # 1. Base case for single digit jump
            ans = dfs(i + 1) 
            
            # 2. Check boundary BEFORE making a two-digit jump
            if i + 1 < len(s): 
                # 3. Correctly grab two characters
                if int(s[i:i+2]) <= 26: 
                    ans += dfs(i + 2)
            
            memo[i] = ans
            return memo[i]
        
        return dfs(0)
        
        return dfs(0)
