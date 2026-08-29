import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        upper bound: at minimum, len(piles) hours 
        '''
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            k = l + (r - l) // 2
            count = 0
            for pile in piles:
                count += math.ceil(float(pile) / k)
            if count > h:
                l = k + 1
            elif count <= h:
                res = k
                r = k - 1
            else:
                return k
        return res