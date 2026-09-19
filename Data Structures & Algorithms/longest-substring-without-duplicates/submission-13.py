class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """ 
        input: string
        output: integer

        plan:
        hash map. key: char, value: index found at 
        res = 0

        l, r = 0, 0

        while r < len(s):
            if s[r] in hashmap and l < map[r]:
                l = map[r] + 1
                res = max r - l + 1
            
            map[r] = r
            r += 1
        """
        mp = {}
        res = 0
        l, r = 0, 0

        while r < len(s):
            c = s[r]
            if c in mp and l <= mp[c]:
                l = mp[c] + 1
            
            res = max(res, r - l + 1)
            
            mp[c] = r
            r += 1
        
        return res