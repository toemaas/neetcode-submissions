class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Strategy: do two binary searches
        First, binary search on the rows
        Once finding the row, binary search the columns
        '''

        lrow, rrow = 0, len(matrix) - 1
        row = 0
        col = len(matrix[0]) - 1
        while lrow <= rrow:
            mid = lrow + (rrow - lrow) // 2
            if matrix[mid][0] > target:
                rrow = mid - 1
            elif matrix[mid][0] < target:
                if matrix[mid][col] >= target:
                    row = mid
                    break
                lrow = mid + 1
            else:
                return True
        lcol, rcol = 0, len(matrix[0]) - 1
        while lcol <= rcol:
            mid = lcol + (rcol - lcol) // 2
            if matrix[row][mid] > target:
                rcol = mid - 1
            elif matrix[row][mid] < target:
                lcol = mid + 1
            else:
                return True
        return False


