class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = height * width
        # largest area = maximize height and width
        # maximize width by starting at both ends
        # height is limited by shorter height.

        l, r = 0, len(heights) - 1
        maxArea = 0

        while l < r:
            maxArea = max(maxArea, (r - l) * min(heights[l], heights[r]))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea