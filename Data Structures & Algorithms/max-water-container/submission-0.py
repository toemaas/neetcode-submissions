class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # height + width
        # height of two bars + index difference
        maxWater = 0
        l, r = 0, len(heights) - 1
        while l < r:
            smaller = min(heights[l], heights[r])
            maxWater = max(smaller * (r - l), maxWater)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxWater
        
        