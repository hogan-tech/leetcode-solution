import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.nextInt = 1

    def popSmallest(self) -> int:
        result = self.nextInt
        if len(self.heap) > 0:
            result = heapq.heappop(self.heap)
        else:
            self.nextInt += 1
        return result

    def addBack(self, num: int) -> None:
        if num < self.nextInt:
            if num not in self.heap:
                heapq.heappush(self.heap, num)


obj = SmallestInfiniteSet()
print(obj)
