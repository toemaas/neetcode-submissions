class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(cur, op, close):
            if op == n and close == n:
                res.append("".join(cur.copy()))
                return

            if op < n:
                cur.append("(")
                dfs(cur, op + 1, close)
                cur.pop()
            if close < op:
                cur.append(")")
                dfs(cur, op, close + 1)
                cur.pop()

        dfs([], 0, 0)
        return res