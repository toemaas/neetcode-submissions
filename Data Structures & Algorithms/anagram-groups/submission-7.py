class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # frequency
        # store frequency as a key in hashset.
        # append to hashset
        hashset = defaultdict(list)
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            hashset[tuple(freq)].append(s)
        
        return list(hashset.values())