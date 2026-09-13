class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # top left -> top right
        # top right -> bot right
        # bot right -> bot left
        # bot left -> top left
        # move inwards
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                temp = matrix[l][l + i]
                matrix[l][l + i] = matrix[r - i][l]
                matrix[r - i][l] = matrix[r][r - i]
                matrix[r][r - i] = matrix[l + i][r]
                matrix[l + i][r] = temp
            l += 1
            r -= 1

