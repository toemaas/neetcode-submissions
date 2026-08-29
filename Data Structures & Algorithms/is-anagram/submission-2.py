class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freqTableS, freqTableT = {}, {}

        for i in range(len(s)):
            freqTableS[s[i]] = 1 + freqTableS.get(s[i], 0)
            freqTableT[t[i]] = 1 + freqTableT.get(t[i], 0)
        return freqTableS == freqTableT