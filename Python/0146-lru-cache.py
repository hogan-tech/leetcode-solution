# time complexity: O(1)
# space complexity: O(n)
from collections import OrderedDict


class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # left -> LRU, right -> MRU
        self.left = ListNode(-1, -1)
        self.right = ListNode(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            oldNode = self.cache[key]
            self.remove(oldNode)

        node = ListNode(key, value)
        self.cache[key] = node
        self.add(node)

        if len(self.cache) > self.capacity:
            lruNode = self.left.next
            self.remove(lruNode)
            del self.cache[lruNode.key]

    def add(self, node):
        prevNode = self.right.prev
        nextNode = self.right

        prevNode.next = node
        nextNode.prev = node
        node.prev = prevNode
        node.next = nextNode

    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode


'''
P <----> Right
   Curr
P <-> Curr <-> Right 
'''

'''
P <-> Curr <-> N
P <-> N
'''


class LRUCache:

    def __init__(self, capacity: int):
        self.cacheDic = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cacheDic:
            self.cacheDic.move_to_end(key)
            return self.cacheDic[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cacheDic:
            self.cacheDic.move_to_end(key)

        self.cacheDic[key] = value
        if len(self.cacheDic) > self.capacity:
            self.cacheDic.popitem(False)


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
obj.put(3, 3)
print(obj.get(2))
obj.put(4, 4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))
