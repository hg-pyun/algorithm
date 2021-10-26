class MyQueue:

    def __init__(self):
        self.store_stack = []
        self.reverse_stack = []
        
    def push(self, x: int) -> None:
        while self.store_stack:
            self.reverse_stack.append(self.store_stack.pop())
        self.store_stack.append(x)
        
        while self.reverse_stack:
            self.store_stack.append(self.reverse_stack.pop())

    def pop(self) -> int:
        if self.store_stack:
            return self.store_stack.pop();

    def peek(self) -> int:
        return self.store_stack[len(self.store_stack) - 1]
        

    def empty(self) -> bool:
        return len(self.store_stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
