# time complexity: O(nlogn + k)
# space complexity: O(n + k)
import bisect


class SnapshotArray:

    def __init__(self, length: int):
        self.id = 0
        self.historyRecords = [[[0, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.historyRecords[index].append([self.id, val])

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snapId: int) -> int:
        snapIndex = bisect.bisect_right(
            self.historyRecords[index], [snapId, 10 ** 9])
        return self.historyRecords[index][snapIndex - 1][1]


snapshotArr = SnapshotArray(4)
snapshotArr.set(0, 15)
print(snapshotArr.snap())
print(snapshotArr.snap())
print(snapshotArr.snap())
print(snapshotArr.get(0, 2))
print(snapshotArr.snap())
print(snapshotArr.snap())
print(snapshotArr.get(0, 0))
