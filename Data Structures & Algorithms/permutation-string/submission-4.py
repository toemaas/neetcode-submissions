class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # window size = len(s1)
        # freq of s1 must match freq of window
        # increment left and right pointers by one
        # decrement freq of s2[l], increase freq of s2[r]
        if len(s1) > len(s2):
            return False
        l, r = 0, len(s1) - 1
        f1 = [0] * 26
        f2 = [0] * 26
        for idx in range(len(s1)):
            f1[ord(s1[idx]) - ord('a')] += 1
            f2[ord(s2[idx]) - ord('a')] += 1
        while r < len(s2):
            if f1 == f2:
                return True
            else:
                f2[ord(s2[l]) - ord('a')] -= 1
                l += 1
                r += 1
                if r < len(s2):
                    f2[ord(s2[r]) - ord('a')] += 1
        return False