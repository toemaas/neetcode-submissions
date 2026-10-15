class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            # append length + # + str
            # 5#wordse
            res.append(str(len(s)) + '#' + s)
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        l = r = 0
        res = []
        while r < len(s):
            if s[r] == '#':
                length = int(s[l:r])
                res.append(s[r + 1:r + length + 1])
                r += length
                l = r + 1
            r += 1
        return res