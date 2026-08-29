class TimeMap:

    def __init__(self):
        self.hashmap = {} # pair: timestamp, value

    def set(self, key: str, value: str, timestamp: int) -> None:
        # append to hashmap
        if key not in self.hashmap:
            self.hashmap[key] = [[timestamp, value]]
        else:
            self.hashmap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        # binary search
        hm = self.hashmap
        if key not in hm:
            return ""

        l, r = 0, len(hm[key]) - 1
        res = ""
        while l <= r:
            m = l + (r - l) // 2
            if hm[key][m][0] > timestamp:
                r = m - 1
            else:
                res = hm[key][m][1]
                l = m + 1
    
        return res