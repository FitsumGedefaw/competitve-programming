class MyQueue:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.popleft()

    def peek(self) -> int:
        return self.stack[0]
        

    def empty(self) -> bool:
        if(len(self.stack) == 0):
            return True
        else:
            return False
