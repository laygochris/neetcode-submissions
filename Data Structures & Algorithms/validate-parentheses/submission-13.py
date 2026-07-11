class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        key = {']':'[', ')':'(', '}':'{'}

        ''' 
        edge cases:
            1. stack not empty at the end
            2. closing parentheses on an empty stack
        '''
    
        for c in s:
            if c not in key:
                print(c)
                stack.append(c)
            elif stack and stack[-1] != key[c] or not stack:
                return False
            else:
                stack.pop()
            
            
        print(stack)
        return len(stack) == 0

            