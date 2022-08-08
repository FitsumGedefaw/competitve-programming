class MyCircularDeque:

    def __init__(self, k: int):
        self.myCQ = deque()
        self.maxLen = k
    def insertFront(self, value: int) -> bool:
        if  len(self.myCQ) < self.maxLen:
            self.myCQ.appendleft(value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if  len(self.myCQ) < self.maxLen:
            self.myCQ.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if not(self.isEmpty()):
            self.myCQ.popleft()
            return True
        else:
            return False
    def deleteLast(self) -> bool:
        if not(self.isEmpty()):
            self.myCQ.pop()
            return True
        else:
            return False

    def getFront(self) -> int:
        if not(self.isEmpty()):
            return self.myCQ[0]
        else:
            return -1

    def getRear(self) -> int:
        if not(self.isEmpty()):
            return self.myCQ[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        if len(self.myCQ) == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if len(self.myCQ) == self.maxLen:
            return True
        else:
            return False
