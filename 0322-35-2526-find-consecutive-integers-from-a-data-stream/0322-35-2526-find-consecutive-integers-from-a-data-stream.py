# time complexity: O(1)
# space complexity: O(1)
class DataStream:
    def __init__(self, value: int, k: int):
        self.val = value
        self.k = k
        self.acc = 0

    def consec(self, num: int) -> bool:
        if num == self.val:
            self.acc += 1
        else:
            self.acc = 0
        if self.acc >= self.k:
            return True
        return False


dataStream = DataStream(4, 3)
print(dataStream.consec(4))
print(dataStream.consec(4))
print(dataStream.consec(4))
print(dataStream.consec(3))
