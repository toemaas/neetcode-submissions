class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1, freq2 = {}, {}

        for c in s:
            freq1[c] = 1 + freq1.get(c, 0)
        
        for c in t:
            freq2[c] = 1 + freq2.get(c, 0)
        
        return freq1 == freq2