class MedianFinder:

    def __init__(self):
        self.max_heap = []   # store smaller numbers
        self.min_heap = []   # store larger numbers  

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)

        x = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, x)

        if len(self.max_heap) < len(self.min_heap):
            y = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -y)
        

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (self.min_heap[0] - self.max_heap[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()