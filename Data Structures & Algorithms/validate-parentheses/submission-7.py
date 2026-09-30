class Solution:
    def isValid(self, s: str) -> bool:
        pair = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c in "[({":
                stack.append(c)
            if c in pair:
                if not stack or stack.pop() != pair[c]:
                    return False
        
        return len(stack) == 0