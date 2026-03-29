class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for c in tokens: 
            if c in "+/-*":
                a = stack.pop()
                b = stack.pop()

                print("a is ", a, " b is ", b)
                
                if c == "+":
                    print("+ received, ", a+b)
                    stack.append(round(a + b))
                elif c == "-":
                    print("- received, ", b-a)
                    stack.append(round(b - a))
                elif c == "*":
                    print("* received, ", a*b)
                    stack.append(round(a * b))
                elif c == "/":
                    print("/ received, ", b/a)
                    stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        
        return stack[0]
