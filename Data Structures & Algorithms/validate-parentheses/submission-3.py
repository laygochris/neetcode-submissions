class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        key = { ')' : '(', '}' : '{', ']' : '['}

        for c in s:
            if c in key:
                if stack and stack[-1] == key[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False