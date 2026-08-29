class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # pair: index, height
        res = 0

        for idx, h in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > h:
                res = max(res, (idx - stack[-1][0]) * stack[-1][1])
                start = stack.pop()[0]
            stack.append([start, h])
        while stack:
            t = stack.pop()
            res = max(res, (len(heights) - t[0]) * t[1])
        return res