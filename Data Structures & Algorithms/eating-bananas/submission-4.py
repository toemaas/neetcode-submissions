class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1, 2, 3, 4
        #     k = 4
        # ceil(k / 2)
        # 4, 10, 23, 25
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = l + (r - l) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / k)
            if time <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res