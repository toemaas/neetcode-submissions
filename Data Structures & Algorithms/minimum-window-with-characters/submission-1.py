class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Z Y X Y Y Z
        # X Z Z Y X
        # Z Z Z X
        # Z Y X Z
        # create a new array consisting of only letters in t from s, keep track of idx as well
        # if duplicate and not complete, check if incrementing l would remove letter from builder
        # if complete and duplicate, then increment until only freq of that letter remain
        # if complete and not duplicate: check length and set equal to res
        # Not duplicate and not complete: add to hashset

        freqT, freqS = {}, {}

        for char in t:
            freqT[char] = 1 + freqT.get(char, 0)
        
        have, need = 0, len(freqT)
        res, reslen = [-1, -1], float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            freqS[c] = 1 + freqS.get(c, 0)

            if c in freqT and freqS[c] == freqT[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < reslen:
                    res = [l, r]
                    reslen = r - l + 1
                freqS[s[l]] -= 1
                if s[l] in freqT and freqS[s[l]] < freqT[s[l]]:
                    have -= 1
                l += 1
        return s[res[0]:res[1] + 1]





