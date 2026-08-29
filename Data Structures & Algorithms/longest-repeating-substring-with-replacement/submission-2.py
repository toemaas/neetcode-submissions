class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # while k > 0:
        # XYYXX check other frequencies <= k
        # keep track of length (r - l) + 1
        # keep track of frequencies and max frequency
        # if max frequency - length <= k:
        #   res = length
        # else:
        #   freq[s[l]] -= 1
        #   l += 1

        freq = {}
        l, r = 0, 0
        maxFreq = 0
        res = 0

        while r < len(s):
            length = r - l + 1
            freq[s[r]] = 1 + freq.get(s[r], 0)
            maxFreq = max(maxFreq, freq[s[r]])

            if length - maxFreq <= k:
                res = max(res, length)
                r += 1
            else:
                freq[s[l]] -= 1
                freq[s[r]] -= 1
                maxFreq = max(maxFreq, freq[s[l]])
                l += 1
        return res