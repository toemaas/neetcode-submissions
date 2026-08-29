class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # for i in range(i, i + k)
        # if pos not added starting at k - 1 index, add curMax
        # if greater move r to it 
        # elif out of range, l += 1
        # else: update curMax

        maxHeap = []
        res = []

        for i in range(len(nums)):
            heapq.heappush(maxHeap, (-nums[i], i))
            if i >= k - 1:
                while maxHeap[0][1] <= i - k:
                    heapq.heappop(maxHeap)
                res.append(-maxHeap[0][0])
        return res
