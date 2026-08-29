class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set for duplicate characters
        # set: yz xz zz
        # if char in hashset:
        # l = hashset[char] + 1
        # else:
        # r += 1
        # key: char, value: idx
        # l, r

        l, r = 0, 0
        hashset = {}
        res = 0

        while r < len(s):
            if s[r] in hashset and hashset[s[r]] >= 0:
                for idx in range(l, hashset[s[r]]):
                    hashset[s[idx]] = -1
                l = hashset[s[r]] + 1
            else:
                res = max(r - l + 1, res)
            hashset[s[r]] = r
            r += 1
        
        return res