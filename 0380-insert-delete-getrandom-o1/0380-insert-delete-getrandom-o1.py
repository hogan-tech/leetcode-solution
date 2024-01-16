# time complexity: O(1)
# space complexity: O(n)
from random import choice


class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.dict:
            lastEle, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[lastEle] = lastEle, idx

            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(1))
print(obj.remove(2))
print(obj.insert(2))
print(obj.getRandom())
print(obj.remove(1))
print(obj.insert(2))
print(obj.getRandom())
