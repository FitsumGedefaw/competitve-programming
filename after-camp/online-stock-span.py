class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        prevSpan = 0
        while self.stack and self.stack[-1][1] <= price:
            span, lastPrice = self.stack.pop()
            prevSpan += span

        self.stack.append((prevSpan + 1, price))
        return prevSpan + 1

        
            
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)