class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        bucket = [[] for i in range(len(nums) + 1)]

        for num, amnt in freq.items():
            bucket[amnt].append(num)
        
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for idx in bucket[i]:
                res.append(idx)
                if len(res) == k:
                    return res
        # freq = {}

        # for num in nums:
        #     freq[num] = 1 + freq.get(num, 0)
        
        # bucket = defaultdict(list)

        # for num, f in freq.items():
        #     bucket[f].append(num)
        # res = []
        # for i in range(len(nums), 0, -1):
        #     for num in bucket[i]:
        #         res.append(num)
        #         if len(res) == k:
        #             return res






















