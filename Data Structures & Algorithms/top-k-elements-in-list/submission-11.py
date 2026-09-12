class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        
        # key: number, value: frequency
        # frequnecy = length of nums, so bucket
        # could have multiple numbers with the same frequency, so list
        # index i = frequency

        bucket = [[] for _ in range(len(nums) + 1)]
        for num, f in freq.items():
            bucket[f].append(num)
        # count backwards for k 
        # can never be 0 frequency
        res = []
        for i in range(len(nums), 0, -1):
            for n in bucket[i]:
                res.append(n)
                k -= 1
                if k == 0:
                    return res