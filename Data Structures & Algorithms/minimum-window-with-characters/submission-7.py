class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        get frequency of t
        need = number of diff chars in t
        sliding window:
        slide right:
        if char in t, add to window map.
        if map[char] == t[char], then increment have

        while have == need: 
            shrink window from left
        
        store min string in res [l, r]
        """
        res, resLen = [], float('inf')
        target, window = {}, {}
        
        for c in t:
            target[c] = 1 + target.get(c, 0)

        need = len(target)
        have = 0
        l = 0

        for r in range(len(s)):
            if s[r] in target:
                window[s[r]] = 1 + window.get(s[r], 0)
                if window[s[r]] == target[s[r]]:
                    have += 1
            
            while have == need:
                if s[l] in target:
                    window[s[l]] -= 1
                    if window[s[l]] < target[s[l]]:
                        have -= 1
                        if r - l + 1 < resLen:
                            resLen = r - l + 1
                            res = [l, r]
                l += 1
        return s[res[0]:res[1] + 1] if res else ""
