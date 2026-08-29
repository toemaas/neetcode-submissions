class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        hashmap { char : index}
        O(n) time and space
        '''
        res = 0
        l, r = 0, 0
        hm = {}
        while r < len(s):
            char = s[r]
            if char in hm:
                l = max(hm[char] + 1, l)
                hm.pop(char)
            else:
                hm[char] = r
                r += 1
                res = max(res, r - l)
        return res