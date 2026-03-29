class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop(len(self.stack)-1)

    def top(self) -> int:
        topval = self.stack[len(self.stack)-1]
        return topval

    def getMin(self) -> int:
        minval = float('inf')
        for n in self.stack:
            minval = min(minval, n)
        return minval
        
