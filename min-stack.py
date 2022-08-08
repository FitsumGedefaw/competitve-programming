class MinStack:

    def __init__(self):
        self.stack = deque()
        self.minStack = deque()
    def push(self, val: int) -> None:
        self.stack.append(val)
        minElement = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(minElement)
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
