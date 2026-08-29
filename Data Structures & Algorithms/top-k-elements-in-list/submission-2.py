import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initial brute force: first pass, create freq table
        # second pass: create a max heap for k: pop from heap
        res = {}
        for num in nums:
            res[num] = 1 + res.get(num, 0)
        minHeap = []
        for num, freq in res.items():
            heapq.heappush(minHeap, (freq, num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        ans = []
        while len(minHeap):
            ans.append(heapq.heappop(minHeap)[1])
        return ans