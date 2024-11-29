#time complexity: O(n)
#space complexity: O(m)
class MovingAverage:

    def __init__(self, size: int):
        self.queue = []
        self.size = size

    def next(self, val: int) -> float:
        self.queue.append(val)
        return sum(self.queue[-self.size:])/min(self.size, len(self.queue))


# Your MovingAverage object will be instantiated and called as such:
obj = MovingAverage(3)
print(obj.next(1))
print(obj.next(10))
print(obj.next(3))
print(obj.next(5))
