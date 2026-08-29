class Solution:
    def isValid(self, s: str) -> bool:
        op = "([{"
        end = ")]}"
        stack = []
        for paren in s:
            if paren in op:
                stack.append(paren)
            else:
                if len(stack) < 1:
                    return False
                openBracket = stack.pop()
                if ((paren == ")" and openBracket != "(") or
                    (paren == "]" and openBracket != "[") or
                    (paren == "}" and openBracket != "{")):
                    return False
        return len(stack) == 0