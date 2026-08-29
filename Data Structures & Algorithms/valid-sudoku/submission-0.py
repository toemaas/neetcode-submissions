class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(0, len(board)):
            for c in range(0, len(board[0])):
                if board[r][c] != ".":
                    boxR = r // 3 * 3 # 0 
                    boxC = c // 3 * 3 # 3
                    # sub-box check
                    for newR in range(boxR, boxR + 3):
                        for newC in range(boxC, boxC + 3):
                            if newR != r and newC != c:
                                if board[newR][newC] == board[r][c]:
                                    return False
                    # row check
                    for col in range(0, 9):
                        if c != col:
                            if board[r][c] == board[r][col]:
                                return False
                    # col check
                    for row in range(0, 9):
                        if r != row:
                            if board[r][c] == board[row][c]:
                                return False
        
        return True