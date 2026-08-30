class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row 1, col 5
        # row // 3 = sub box row
        # col // 3 = sub box col
        # 0, 1
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [[set() for i in range(3)] for i in range(3)]

        for r in range(len(board)):
            for c in range(len(board[0])):
                num = board[r][c]
                if num != ".":
                    if num in rows[r]:
                        return False
                    else:
                        rows[r].add(num)
                    if num in cols[c]:
                        return False
                    else:
                        cols[c].add(num)
                    row = r // 3
                    col = c // 3
                    if num in boxes[row][col]:
                        return False
                    else:
                        boxes[row][col].add(num)
        return True