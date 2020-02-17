class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = None
        self.stack = []

    def push(self, x: int) -> None:
        if self.min is None:
            self.min = x
        elif x < self.min:
            self.min = x
        self.stack.append(x)

    def pop(self) -> None:
        if len(self.stack) > 0:
            if self.stack.pop() == self.min:
                if len(self.stack) > 0:
                    self.min = min(self.stack)
                else:
                    self.min = None

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()