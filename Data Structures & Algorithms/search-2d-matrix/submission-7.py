class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lCol, lRow = 0, len(matrix[0]) - 1
        l, r = 0, len(matrix[0]) - 1
        top, bot = 0, len(matrix) - 1

        while l <= r and top <= bot:
            mRow = top + (bot - top) // 2
            
            if target >= matrix[mRow][lCol] and target <= matrix[mRow][lRow]:
                left, right = 0, len(matrix[0]) - 1
                while left <= right:
                    m = left + (right - left) // 2
                    if matrix[mRow][m] == target:
                        return True
                    elif matrix[mRow][m] > target:
                        right = m - 1
                    else:
                        left = m + 1
                return False
            elif target < matrix[mRow][lCol]:
                bot = mRow - 1
            else:
                top = mRow + 1
            
        return False