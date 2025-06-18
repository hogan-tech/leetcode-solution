# time complexity: O(logn)
# space complexity: O(n)
import heapq


class MedianFinder:

    def __init__(self):
        self.maxHp=[]
        self.minHp=[]
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHp, -num)
        heapq.heappush(self.minHp, -heapq.heappop(self.maxHp))
        if len(self.maxHp) < len(self.minHp):
            heapq.heappush(self.maxHp, -heapq.heappop(self.minHp))

    def findMedian(self) -> float:
        if len(self.maxHp) > len(self.minHp):
            return -self.maxHp[0]
        else:
            return float(-self.maxHp[0] + self.minHp[0]) / 2


medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
print(medianFinder.findMedian())
medianFinder.addNum(3)
print(medianFinder.findMedian())
