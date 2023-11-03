class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [-1] * k
        self.maxSize = k
        self.head = 0
        self.tail = -1
        
    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.tail = (self.tail + 1) % self.maxSize
            self.arr[self.tail] = value
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            if self.head == self.tail: #only one element left
                self.head, self.tail = 0, -1
            else:
                self.head = (self.head + 1) % self.maxSize
            return True
        return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.arr[self.head]
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.arr[self.tail]
        return -1

    def isEmpty(self) -> bool:
        return self.tail == -1

    def isFull(self) -> bool:
        return not self.isEmpty() and (self.tail + 1) % self.maxSize == self.head


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()