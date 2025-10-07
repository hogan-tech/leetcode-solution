# time complexity: O(1)
# space complexity: O(n)
from collections import OrderedDict, defaultdict


class LFUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.frequencies = defaultdict(OrderedDict)
        self.minf = 0
        self.capacity = capacity

    def insert(self, key, frequency, value):
        self.cache[key] = (frequency, value)
        self.frequencies[frequency][key] = value

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        frequency, value = self.cache[key]
        del self.frequencies[frequency][key]
        if not self.frequencies[frequency]:
            del self.frequencies[frequency]
            if frequency == self.minf:
                self.minf += 1
        self.insert(key, frequency + 1, value)
        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        if key in self.cache:
            frequency = self.cache[key][0]
            self.cache[key] = (frequency, value)
            self.get(key)
            return
        if self.capacity == len(self.cache):
            keyToDelete, frequency = self.frequencies[self.minf].popitem(
                last=False)
            del self.cache[keyToDelete]
        self.minf = 1
        self.insert(key, 1, value)


lfu = LFUCache(2)
lfu.put(1, 1)
lfu.put(2, 2)
print(lfu.get(1))
lfu.put(3, 3)
print(lfu.get(2))
print(lfu.get(3))
lfu.put(4, 4)
print(lfu.get(1))
print(lfu.get(3))
print(lfu.get(4))
