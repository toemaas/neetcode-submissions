class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
        return ",".join(res) + "#" + "".join(strs)

    def decode(self, s: str) -> List[str]:
        print(s)
        start = s.index("#") # 55#HelloWorld
        st = s.index("#") + 1 # 3
        lengths = s[0:start]
        lenArr = lengths.split(",") # 5,5
        res = []
        if lenArr[0] == '':
            return res
        for l in lenArr:
            length = int(l)
            res.append(s[st:st + length])
            st += length
        return res