class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)
        
        if len(self.maxHeap) - len(self.minHeap) > 1:
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -val)       
            
        elif self.minHeap and -self.maxHeap[0] > self.minHeap[0]:
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -val)  
            
            if len(self.minHeap) - len(self.maxHeap) > 1:
                val = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -val)  
            

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        
        elif len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        
        return self.minHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()