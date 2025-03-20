# time complexity: O(n*p)
# space complexity: O(n)
from collections import defaultdict


class MapSum:
    def __init__(self):
        self.wordMap = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        self.wordMap[key] = val

    def sum(self, prefix: str) -> int:
        result = 0
        for key, val in self.wordMap.items():
            if key.startswith(prefix):
                result += val
        return result


mapSum = MapSum()
mapSum.insert("apple", 3)
print(mapSum.sum("ap"))
mapSum.insert("app", 2)
print(mapSum.sum("ap"))
