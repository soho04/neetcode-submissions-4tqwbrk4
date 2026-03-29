class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        counter = 0

        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
                counter += 1
            elif stack:
                if c == ')' and stack[counter-1] == '(' and stack:
                    stack.pop(counter-1)
                    counter -= 1
                    s = s.replace('()', '')
                elif c == '}' and stack[counter-1] == '{' and stack:
                    stack.pop(counter-1)
                    counter -= 1
                    s = s.replace('{}', '')
                elif c == ']' and stack[counter-1] == '[' and stack:
                    stack.pop(counter-1)
                    counter -= 1
                    s = s.replace('[]', '')
            
        print(s)

        return True if not s else False




        