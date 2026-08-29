import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # for i in range(i, i + k)
        # if pos not added starting at k - 1 index, add curMax
        # if greater move r to it 
        # elif out of range, l += 1
        # else: update curMax

        maxHeap = []
        for i in range(k - 1):
            heapq.heappush(maxHeap, (-1 * nums[i], i))
        res = []
        l = 0
        for r in range(k - 1, len(nums)):
            heapq.heappush(maxHeap, (-1 * nums[r], r))
            idx = maxHeap[0][1]
            while idx < l or idx > r:
                heapq.heappop(maxHeap)
                idx = maxHeap[0][1]
            res.append(nums[idx])
            l += 1
        return res
