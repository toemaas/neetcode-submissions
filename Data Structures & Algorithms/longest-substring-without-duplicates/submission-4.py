class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        hashmap { char : index}
        O(n) time and space
        '''
        res = 0
        l, r = 0, 0
        hm = {}
        for r in range(len(s)):
            char = s[r]
            if char in hm:
                l = max(hm[char] + 1, l)
            hm[char] = r
            res = max(res, r - l + 1)
        return res