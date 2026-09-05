class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = {}
        cols = {}

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rows[r] = 1
                    cols[c] = 1
        
        for row in rows.keys():
            for c in range(len(matrix[0])):
                matrix[row][c] = 0

        for col in cols.keys():
            for r in range(len(matrix)):
                matrix[r][col] = 0