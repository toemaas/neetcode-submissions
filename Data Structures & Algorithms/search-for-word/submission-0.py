class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        hs = set()
        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r, c) in hs or r >= len(board) or r < 0 or c >= len(board[0]) or c < 0 or board[r][c] != word[i]:
                return False
            # if word in hashset or r, c out of bounds:
            #   return
            
            hs.add((r, c))
            res = (
                dfs(r - 1, c, i + 1) or
                dfs(r, c - 1,  i + 1) or
                dfs(r + 1, c, i + 1) or
                dfs(r, c + 1, i + 1)
            )
            hs.remove((r, c))
            return res
            # check if word done
            # if it is, return true
            
            # add r, c to stack
            # dfs four corners11

        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False