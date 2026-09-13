class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)

        # idx 0 = 0th row, 0th col, 0th box
        # idx 5 = 5th row, 5th col, 5th box
        # how do we determine the box? 
        # [8, 8] = box 7
        # 8 / 3 = 1 * 3
        # 8 // 3 = 2
        # 5 + 2 = 5
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != '.':
                    char = board[r][c]
                    idx = (r // 3) * 3 + c // 3
                    if char in rows[r] or char in cols[c] or char in box[idx]:
                        return False
                    rows[r].add(char)
                    cols[c].add(char)
                    box[idx].add(char)
        return True