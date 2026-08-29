class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find row = idx % col
        # l, r = 0, len(matrix) * len(matrix[0]) - 1
        # midpoint = l + (r - l) // 2 = 5
        # 5 = matrix[1][1]
        # row = mid // len(matrix[0])
        # col = mid % len(matrix[0]

        # l = row * len(matrix[0]) + col + 1
        # r = row * len(matrix[0]) + col - 1

        rowLength, colLength = len(matrix), len(matrix[0])
        l, r = 0, rowLength * colLength - 1
        while l <= r:
            mid = l + (r - l) // 2
            row = mid // colLength
            col = mid % colLength

            if target > matrix[row][col]:
                l = mid + 1
            elif target < matrix[row][col]:
                r = mid - 1
            else:
                return True
        
        return False
