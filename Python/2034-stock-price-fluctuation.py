# time complexity: O(nlogn)
# space complexity: O(n)
from heapq import heappop, heappush


class StockPrice:
    def __init__(self):
        self.latestTime = 0
        self.timestampMap = {}

        self.maxHeap = []
        self.minHeap = []

    def update(self, timestamp: int, price: int) -> None:
        self.timestampMap[timestamp] = price
        self.latestTime = max(self.latestTime, timestamp)

        heappush(self.minHeap, (price, timestamp))
        heappush(self.maxHeap, (-price, timestamp))

    def current(self) -> int:
        return self.timestampMap[self.latestTime]

    def maximum(self) -> int:
        price, timestamp = self.maxHeap[0]

        while -price != self.timestampMap[timestamp]:
            heappop(self.maxHeap)
            price, timestamp = self.maxHeap[0]

        return -price

    def minimum(self) -> int:
        price, timestamp = self.minHeap[0]

        while price != self.timestampMap[timestamp]:
            heappop(self.minHeap)
            price, timestamp = self.minHeap[0]

        return price


'''
{
    1: 3
    2: 5
}

max = 10 min = 10 latestIdx = [1] <- maxHp
max = 10 min = 3  latestIdx = [1, 2] <- maxHp
'''

stockPrice = StockPrice()
stockPrice.update(1, 10)
stockPrice.update(2, 5)
print(stockPrice.current())
print(stockPrice.maximum())
stockPrice.update(1, 3)
print(stockPrice.maximum())
stockPrice.update(4, 2)
print(stockPrice.minimum())
