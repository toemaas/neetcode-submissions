class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1

        while l <= r:
            m = l + (r - l) // 2
            mRow = m // COLS
            mCol = m % COLS
            if matrix[mRow][mCol] == target:
                return True
            elif matrix[mRow][mCol] < target:
                l = m + 1
            else:
                r = m - 1
        return False