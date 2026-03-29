class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [] ## Store minimum values 

    def push(self, val: int) -> None:
        self.stack.append(val)

        minimum_val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(minimum_val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    # How to get it to run constant?

    def getMin(self) -> int:
        return self.minStack[-1]
        