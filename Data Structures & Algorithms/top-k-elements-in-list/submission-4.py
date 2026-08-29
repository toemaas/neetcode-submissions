class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}

        for num in nums:
            freqMap[num] = 1 + freqMap.get(num, 0)
        
        bucket = [[] for i in range(len(nums) + 1)]

        for num, freq in freqMap.items():
            bucket[freq].append(num)
        
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
            if len(res) == k:
                return res

            