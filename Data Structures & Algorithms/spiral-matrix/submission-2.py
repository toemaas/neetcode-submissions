class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # keep track of 4 boundaries: row start and end, col start and end
        # decrement 
        l, r = 0, len(matrix[0]) # left col, right col
        t, b = 0, len(matrix) # top row, bottom row
        res = []
        while l < r and t < b:

            for i in range(l, r):
                res.append(matrix[t][i])
            t += 1
            for i in range(t, b):
                res.append(matrix[i][r - 1])
            r -= 1
            if not (l < r and t < b):
                break
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[b - 1][i])
            b -= 1
            for i in range(b - 1, t - 1, -1):
                res.append(matrix[i][l])
            l += 1
        
        return res
