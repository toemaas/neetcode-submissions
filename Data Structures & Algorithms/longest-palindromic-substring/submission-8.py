class Solution:
    def longestPalindrome(self, s: str) -> str:
        """ 
        input: string of digits and english letters
        output: string palindrome

        plan:

        for each char:
            act as if its th center and expand outwards. two pointer. check if they match and continue
            for even lengthed palindromes, start at i and i + 1
        
        edge cases: "a", "ab", "aa"
        """
        res = [0, -1]

        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l > res[1] - res[0]:
                    res = [l, r]
                l -= 1
                r += 1

            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l > res[1] - res[0]:
                    res = [l, r]
                l -= 1
                r += 1

        return s[res[0]:res[1] + 1]