# time complexity: O(n)
# space complexity: O(n)
from typing import List


class RLEIterator:
    def __init__(self, encoding: List[int]):
        self.encoding = encoding[::-1]

    def next(self, n: int) -> int:
        acc = 0
        while acc < n:
            if not self.encoding:
                return -1
            times, num = self.encoding.pop(), self.encoding.pop()
            acc += times
        self.encoding.append(num)
        self.encoding.append(acc - n)
        return num


rLEIterator = RLEIterator([3, 8, 0, 9, 2, 5])
print(rLEIterator.next(2))
print(rLEIterator.next(1))
print(rLEIterator.next(1))
print(rLEIterator.next(2))
