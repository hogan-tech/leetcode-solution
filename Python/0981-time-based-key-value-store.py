# set()
# time complexity: O(m*l)
# space complexity: O(l)
# get()
# time complexity: O(n*timestamp*l)
# space complexity: O(1)
from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        currKeyList = self.map[key]
        if timestamp < currKeyList[0][0]:
            return ""
        left = 0
        right = len(currKeyList)
        while left < right:
            mid = (left + right) // 2
            midTime, midVal = currKeyList[mid]
            if midTime == timestamp:
                return midVal
            if midTime < timestamp:
                left = mid + 1
            else:
                right = mid
        return "" if right == 0 else currKeyList[right-1][1]
'''
{
    'foo': [[1, 'bar'], [4, 'bar2]]
}
'''
timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
print(timeMap.get("foo", 1))
print(timeMap.get("foo", 3))
timeMap.set("foo", "bar2", 4)
print(timeMap.get("foo", 4))
print(timeMap.get("foo", 5))
