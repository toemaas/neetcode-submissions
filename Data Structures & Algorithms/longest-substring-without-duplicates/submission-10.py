class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #hash map key: char, value: index

        # sliding window
        # if char in hashmap:
        # for l in range(char index)
        # subtract from hashmap
        # subtract from substring length

        l, r = 0, 0
        mp = {}
        res = 0
        while r < len(s):
            char = s[r]
            if char in mp and mp[char] >= l:
                l = mp[char] + 1
            res = max(res, r - l + 1)
            mp[char] = r
            r += 1
        return res