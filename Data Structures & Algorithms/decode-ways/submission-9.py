class Solution:
    def numDecodings(self, s: str) -> int:
        """
        input: string of digits
        output: int ways to decode

        plan:

        at each step: can choose either one digit 1-9 or two digits within 10-19 and 20-26
        base case: 0: return 0
        dp1 = num ways to decode n - 1
        dp2 = num ways to decode n
        381341
        """
        dp = dp2 = 0
        dp1 = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp = 0
            else:
                dp = dp1
            
            if i + 1 < len(s) and (s[i] == "1" or
                s[i] == "2" and s[i + 1] in "0123456"):
                dp += dp2

            dp, dp1, dp2 = 0, dp, dp1
        return dp1

