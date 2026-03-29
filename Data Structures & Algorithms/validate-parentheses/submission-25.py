class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for char in s:
            
            if stack:
                if (char == "]" and stack[-1] == "[") or (char == ")" and stack[-1] == "(") or (char == "}" and stack[-1] == "{"):
                    stack.pop()
                    continue

            stack.append(char)

        
        return True if stack == [] else False



                




        

            
