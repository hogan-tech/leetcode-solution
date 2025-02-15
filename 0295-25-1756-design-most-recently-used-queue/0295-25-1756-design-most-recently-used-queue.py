# time complexity: O(log^2 n)
# space complexity: O(n)
from sortedcontainers import SortedList


class MRUQueue:

    def __init__(self, n: int):
        self.queue = SortedList((position, value)
                                for position, value in enumerate(range(1, n + 1)))

    def fetch(self, k: int) -> int:
        _, value = self.queue.pop(k - 1)
        nextPosition = self.queue[-1][0] + 1 if self.queue else 0
        self.queue.add((nextPosition, value))
        return value


mRUQueue = MRUQueue(8)
print(mRUQueue.fetch(3))
print(mRUQueue.fetch(5))
print(mRUQueue.fetch(2))
print(mRUQueue.fetch(8))

[1, 2, 3, 4, 5, 6, 7, 8]
