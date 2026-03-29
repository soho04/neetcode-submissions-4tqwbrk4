class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:

            if token in "+-*/":

                b, a = int(stack.pop()), int(stack.pop())

                print(b, a)

                if token == "+":
                    stack.append(b+a)

                elif token == "-":
                    stack.append(a-b)

                elif token == "*":
                    stack.append(a*b)

                else:

                    print(math.floor(a//b))
                    stack.append(int(a/b))

            else:
                stack.append(token)

        return int(stack[-1])

        # 9, 4 -> b = 4, a = 9
                            #                                            y   
        # tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

        # 22
