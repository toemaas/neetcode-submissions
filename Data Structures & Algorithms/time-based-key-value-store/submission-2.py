class TimeMap:

    def __init__(self):
        self.hash = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        keys = self.hash[key]
        l, r = 0, len(keys) - 1
        res = ""

        while l <= r:
            m = l + (r - l) // 2
            if keys[m][1] < timestamp:
                res = keys[m][0]
                l = m + 1
            elif keys[m][1] > timestamp:
                r = m - 1
            else:
                return keys[m][0]
        
        return res
                

        
        # hashmap key: [(value, timestamp), (value, timestamp)]
        # keys = hashmap[key]
        # l, r
        # while l <= r:
        #   m = l + (r - l) // 2
        #   keys[m][1]
        #   keys[l][1]
        
