class Solution:
    def isValid(self, s: str) -> bool:
        key = {')' : '(', ']' : '[', '}' : '{'}
        stack = []

        for c in s:
            if c in key:
                if stack and stack[-1] == key[c]:
                    stack.pop()
                else: 
                    return False
            else: 
                stack.append(c)

        if stack:
            return False
        else:
            return True