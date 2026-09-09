class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # add c
        # dfs up
        # pop
        # base case: out of bounds or char not equal to word
        # def dfs(r, c, i)
        #   if out of bounds:
        #       return False
        #   elif board[r][c] != word[i] or (r, c) in hashmap:
        #       return False
        #   elif i = len(word) - 1:
        #       return True
        #   else:
        #       hashmap[(r, c)] = True
        #    res = (dfs up or dfs down or dfs left or dfs right)
        #       hashmap.remove(r, c)

        hashmap = {}
        def dfs(r, c, i):
            if (r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or 
            board[r][c] != word[i] or (r, c) in hashmap):
                return False
            elif i == len(word) - 1:
                return True
            hashmap[(r, c)] = True
            res = (dfs(r - 1, c, i + 1) or dfs(r + 1, c, i + 1) 
                    or dfs(r, c - 1, i + 1) or dfs(r, c + 1, i + 1))
            hashmap.pop((r, c))
            return res
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
        
        return False