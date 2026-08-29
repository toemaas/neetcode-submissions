class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for s in strs:
        # get the frequency of s
        # map[frequency].append(s)
        # return map values as a list

        m = {}

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            freq = tuple(count)

            if freq in m:
                m[freq].append(s)
            else:
                m[freq] = [s]

        return list(m.values())