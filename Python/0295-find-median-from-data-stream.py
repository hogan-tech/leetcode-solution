# time complexity: O(logn)
# space complexity: O(n)
import heapq


class MedianFinder:

    def __init__(self):
        self.largeMinHeap = []
        self.smallMaxHeap = []

    def addNum(self, num: int) -> None:
        if not self.smallMaxHeap or -self.smallMaxHeap[0] >= num:
            heapq.heappush(self.smallMaxHeap, -num)
        else:
            heapq.heappush(self.largeMinHeap, num)

        if len(self.smallMaxHeap) > len(self.largeMinHeap) + 1:
            heapq.heappush(self.largeMinHeap, -
                           heapq.heappop(self.smallMaxHeap))
        elif len(self.smallMaxHeap) < len(self.largeMinHeap):
            heapq.heappush(self.smallMaxHeap, -
                           heapq.heappop(self.largeMinHeap))
        return

    def findMedian(self) -> float:
        if len(self.largeMinHeap) == len(self.smallMaxHeap):
            return (self.largeMinHeap[0] - self.smallMaxHeap[0]) / 2.0
        return float(-self.smallMaxHeap[0])


medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
print(medianFinder.findMedian())
medianFinder.addNum(3)
print(medianFinder.findMedian())
