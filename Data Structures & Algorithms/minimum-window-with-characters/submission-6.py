class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = {}

        for c in t:
            freq[c] = 1 + freq.get(c, 0)
        
        res = [-1, float('inf')]
        l = 0
        have = len(freq)
        need = 0
        for r in range(len(s)):
            if s[r] in freq:
                freq[s[r]] -= 1
                if freq[s[r]] == 0:
                    need += 1
            
            while l <= r and have == need:
                if r - l < res[1] - res[0]:
                    res = [l, r]
                if s[l] in freq:
                    freq[s[l]] += 1
                    if freq[s[l]] == 1:
                        need -= 1
                l += 1

        return s[res[0]:res[1] + 1] if res[1] != float('inf') else ""