# Constructor()
# time complexity: O(1)
# space complexity: O(n)
# AddRange()
# time complexity: O(n)
# space complexity: O(n)
# RemoveRange()
# time complexity: O(n)
# space complexity: O(n)
# QueryRange()
# time complexity: O(logn)
# space complexity: O(n)
class RangeModule:

    def __init__(self):
        self.ranges = []

    def checkIntervals(self, left: int, right: int):
        minRange = 0
        maxRange = len(self.ranges) - 1
        mid = len(self.ranges) // 2
        while mid >= 1:
            while minRange + mid < len(self.ranges) and self.ranges[minRange + mid - 1][1] < left:
                minRange += mid
            while maxRange - mid >= 0 and self.ranges[maxRange - mid + 1][0] > right:
                maxRange -= mid
            mid //= 2
        return minRange, maxRange

    def addRange(self, left: int, right: int) -> None:
        if not self.ranges or self.ranges[-1][1] < left:
            self.ranges.append((left, right))
            return

        if self.ranges[0][0] > right:
            self.ranges.insert(0, (left, right))
            return

        minRange, maxRange = self.checkIntervals(left, right)
        
        updatedLeft = min(self.ranges[minRange][0], left)
        updatedRight = max(self.ranges[maxRange][1], right)
        self.ranges[minRange:maxRange + 1] = [(updatedLeft, updatedRight)]

    def queryRange(self, left: int, right: int) -> bool:
        if not self.ranges:
            return False
        minRange, maxRange = self.checkIntervals(left, right)
        return self.ranges[minRange][0] <= left and right <= self.ranges[minRange][1]

    def removeRange(self, left: int, right: int) -> None:
        if not self.ranges or self.ranges[0][0] > right or self.ranges[-1][1] < left:
            return
        minRange, maxRange = self.checkIntervals(left, right)
        updatedRanges = []
        k = minRange
        while k <= maxRange:
            if self.ranges[k][0] < left:
                updatedRanges.append((self.ranges[k][0], left))
            if self.ranges[k][1] > right:
                updatedRanges.append((right, self.ranges[k][1]))
            k += 1

        self.ranges[minRange: maxRange + 1] = updatedRanges


# Your RangeModule object will be instantiated and called as such:
obj = RangeModule()
obj.addRange(10, 20)
obj.removeRange(14, 16)
print(obj.queryRange(10, 14))
print(obj.queryRange(13, 15))
print(obj.queryRange(16, 17))
