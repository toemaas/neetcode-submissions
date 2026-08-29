class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        boxes = defaultdict(list)
        # 0, 1 = 1
        # 1, 0 = 3
        # 2, 0 = 6
        # 2, 2 = 8
        for r in range(0, 9):
            for c in range(0, 9):
                num = board[r][c] # 0, 4 sub box 1
                if num != ".":
                    # check if in row already
                    if num in rows[r]:
                        return False
                    else:
                        rows[r].append(num)
                    # check if in col already
                    if num in cols[c]:
                        return False
                    else:
                        cols[c].append(num)
                    # check if in sub box already
                    box = r // 3 * 3 + c // 3
                    if num in boxes[box]:
                        return False
                    else:
                        boxes[box].append(num)
        return True