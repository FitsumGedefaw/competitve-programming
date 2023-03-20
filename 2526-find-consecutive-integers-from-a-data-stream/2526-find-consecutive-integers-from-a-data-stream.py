class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.dataStream = []
        self.lastIdxOfNonValueNum = -1

    def consec(self, num: int) -> bool:
        self.dataStream.append(num)
        n = len(self.dataStream)
        
        if num != self.value:
            self.lastIdxOfNonValueNum = n - 1
        
        if n < self.k or self.lastIdxOfNonValueNum >= n - self.k:
            return False
        
        return True
        
        
    
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)