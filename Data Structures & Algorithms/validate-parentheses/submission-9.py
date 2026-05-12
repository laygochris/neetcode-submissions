class Solution:
    def isValid(self, s: str) -> bool:
        key = {')' : '(', '}' : '{', ']' : '['}
        stack = []

        for c in s:
            if c in key:
                if stack and stack[-1] != key[c]:
                    return False
                # if its closing, have to check stack
                if not stack:
                    return False
                stack.pop()
                
            else:
                stack.append(c)
        
        return len(stack) == 0