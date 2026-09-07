class Solution:
    def trap(self, height: List[int]) -> int:
        
        water = 0

        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[0], height[-1]
        while l < r:
            if height[l] <= height[r]:
                l += 1
                maxLeft = max(maxLeft, height[l])
                water += maxLeft - min(height[l], maxLeft)
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                water += maxRight - min(height[r], maxRight)
            print(maxLeft)
        
        return water