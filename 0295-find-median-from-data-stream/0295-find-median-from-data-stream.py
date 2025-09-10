class MedianFinder:

    def __init__(self):
        self.minHp = []
        self.maxHp = []
        

    def addNum(self, num: int) -> None:
        heappush(self.maxHp, -num)
        heappush(self.minHp, -heappop(self.maxHp))
        if len(self.maxHp) < len(self.minHp):
            heappush(self.maxHp, -heappop(self.minHp))
        

    def findMedian(self) -> float:
        if len(self.maxHp) > len(self.minHp):
            return -self.maxHp[0]
        else:
            return float(-self.maxHp[0] + self.minHp[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()