class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for c in s:
            if c == '(' or c == '{' or c == '[': # Add opening brackets to stack
                stack.append(c) 

            elif stack:

                if c == ')' and stack[len(stack)-1] == '(': # Check if 
                    stack.pop(len(stack)-1)
                    s = s.replace('()', '')

                elif c == '}' and stack[len(stack)-1] == '{':
                    stack.pop(len(stack)-1)
                    s = s.replace('{}', '')

                elif c == ']' and stack[len(stack)-1] == '[':
                    stack.pop(len(stack)-1)
                    s = s.replace('[]', '')
            
        print(s)

        return True if not s else False




        