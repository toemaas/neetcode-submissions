class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        26 characters
        AAABABAAAAA
        idea:
        sliding window
        keep track of the index of the first encounter of a different char
        decrement the k counter. if it's 0, move the left pointer to the index
        of the first diff char
        '''
        count = {}
        res = 0
        l =  0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max((r - l + 1), res)
        return res
                
