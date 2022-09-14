class MyQueue:

    def __init__(self):
        self.stack = []
        self.helper = []

    def push(self, x: int) -> None:
        self.stack.append(x)
            
    def pop(self) -> int:
        while len(self.stack) > 1:
            self.helper.append(self.stack[-1])
            self.stack.pop()
        value = self.stack.pop()
        while self.helper:
            self.stack.append(self.helper[-1])
            self.helper.pop()
        return value

    def peek(self) -> int:
        while self.stack:
            self.helper.append(self.stack[-1])
            value = self.stack.pop()
        while self.helper:
            self.stack.append(self.helper[-1])
            self.helper.pop()
        return value

    def empty(self) -> bool:
        return len(self.stack) == 0
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
