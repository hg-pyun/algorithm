class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, x: int) -> None:
        if self.min is None:
            self.min = x
        else:
            self.min = min(x, self.min)
        
        self.stack.append(x)
        
    def pop(self) -> None:
        self.stack.pop()
        if(len(self.stack) > 0):
            self.min = self.stack[0]
            for n in self.stack:
                self.min = min(n, self.min)
        else:
            self.min = None

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
