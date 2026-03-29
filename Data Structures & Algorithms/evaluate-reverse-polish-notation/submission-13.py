class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:

            stack.append(token)

            if token in "+-*/":
                
                stack.pop()
                a = int(stack.pop())
                b = int(stack.pop())

                if token == "+":
                    res = a + b

                elif token == "-":
                    res = (b-a)

                elif token == "*":
                    res = (a*b)

                else:
                    res = b / a

                stack.append(res)

        return int(stack[-1])
