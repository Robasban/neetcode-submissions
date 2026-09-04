class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = None

    def push(self, val: int) -> None:
        if (self.minVal == None or val < self.minVal):
            self.minVal = val
        self.stack.append(val)

    def pop(self) -> None:
        self.stack = self.stack[0:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
