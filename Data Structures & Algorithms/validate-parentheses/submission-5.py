class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren = {"}" : "{", ")" : "(", "]" : "["}

        for c in s:
            if c in paren:
                if not stack or stack.pop() != paren[c]:
                    return False
            else:
                stack.append(c)
        
        return not stack