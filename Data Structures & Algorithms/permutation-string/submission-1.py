class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        freq = Counter(s1)
        # idea: have a frequency map of each letter. 26 letters
        # sliding window of the length of s1
        # iterate through s2, checking if the frequency map is equal
        # O(n * 26)
        l, r = 0, len(s1) - 1
        while r < len(s2):
            freq2 = Counter(s2[l:r + 1])
            print(freq2)
            if freq == freq2:
                return True
            l += 1
            r += 1
        return False