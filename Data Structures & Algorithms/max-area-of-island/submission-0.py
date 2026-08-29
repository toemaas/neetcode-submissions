class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1 ,0], [-1, 0], [0, 1], [0, -1]]
        islandArea = 0
        rows, cols, = len(grid), len(grid[0])

        def dfs(r, c):
            nonlocal currArea
            if (r < 0 or c < 0 or r >= rows or c >= cols 
                or grid[r][c] == 0):
                return 0
            
            currArea += 1
            grid[r][c] = 0
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    currArea = 0
                    dfs(r, c)
                    islandArea = max(currArea, islandArea)
        
        return islandArea