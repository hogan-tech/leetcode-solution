from typing import List


class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.map:
            self.map[key]: List = []
        self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.map:
            return ""

        if timestamp < self.map[key][0][0]:
            return ""

        left, right = 0, len(self.map[key])

        while left < right:
            mid = left + (right - left) // 2
            if self.map[key][mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
        return "" if right == 0 else self.map[key][right-1][1]


# Your TimeMap object will be instantiated and called as such:
timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
print(timeMap.get("foo", 1))
print(timeMap.get("foo", 3))
timeMap.set("foo", "bar2", 4)
print(timeMap.get("foo", 4))
print(timeMap.get("foo", 5))
