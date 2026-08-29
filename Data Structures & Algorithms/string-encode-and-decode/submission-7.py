class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = []
        for s in strs:
            res.append(str(len(s)))
        return ",".join(res) + "#" + "".join(strs)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        start = s.index("#")
        st = s.index("#") + 1
        lengths = s[0:start]
        lenArr = lengths.split(",")
        res = []
        for l in lenArr:
            length = int(l)
            res.append(s[st:st + length])
            st += length
        return res