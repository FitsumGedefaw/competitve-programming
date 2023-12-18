class OrderedStream:

    def __init__(self, n: int):
        self.inserted = {}
        self.currPos = 1      

    def insert(self, idKey: int, value: str) -> List[str]:
        self.inserted[idKey] = value
        if idKey > self.currPos:
            return []
        res = [value]
        self.currPos = idKey + 1
        while self.currPos in self.inserted:
            res.append(self.inserted[self.currPos])
            self.currPos += 1
        
        return res


        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)