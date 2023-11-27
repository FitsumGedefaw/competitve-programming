class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.currPos = 0        

    def next(self, n: int) -> int:
        toBeExahusted = n
        while self.currPos < len(self.encoding) and toBeExahusted > self.encoding[self.currPos]:
            toBeExahusted -= self.encoding[self.currPos]
            self.currPos += 2
        
        if self.currPos >= len(self.encoding):
            return -1
        
        self.encoding[self.currPos] -= toBeExahusted
        return self.encoding[self.currPos + 1]
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)