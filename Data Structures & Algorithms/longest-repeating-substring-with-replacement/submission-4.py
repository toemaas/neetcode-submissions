class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        input: string of chars
        output: integer: length of substring

        plan:
        length of substr - highest freq char <= k

        for r in range(len(s)):
            increment char freq
            maxFreq = max(maxFreq, char freq)    
            while l < r and len substr - maxFreq > k:
                decrement s[l] freq
                l += 1
            
            res = max(res, length)
        """
        res = 0
        mp = defaultdict(int)
        maxFreq = 0
        l = 0

        for r in range(len(s)):
            c = s[r]
            mp[c] += 1
            maxFreq = max(maxFreq, mp[c])
            while (r - l + 1) - maxFreq > k:
                mp[s[l]] -= 1
                l += 1
            
            res = max(res, r - l  + 1)
        
        return res