class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        for n in s:
            if n not in table:
                stack.append(n)
            elif not stack or table[n] != stack.pop():
                return False
        
        return len(stack) == 0
                