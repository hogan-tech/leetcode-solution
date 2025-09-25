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
    '''
    left <-> (1, 1) <-> (2,2) <-> right
    left <-> (2,2) <-> (1,1) <-> right
    left <-> (2,2) <-> (1,1) <-> right
    cache = {1:(1,1), 2:(2,2)}

    left <-> (2,2) <-> (1,1) <-> (3,3) <-> right 
    (Now size = 3 > capacity → evict LRU = left.next = (2,2). Remove (2,2))
    left <-> (1,1) <-> (3,3) <-> right
    cache = {1:(1,1), 3:(3,3)}
    '''
    def add(self, node):
        prevNode = self.right.prev
        nextNode = self.right

        prevNode.next = node
        nextNode.prev = node
        node.prev = prevNode
        node.next = nextNode
    '''
    left <-> (2,2) <-> (1,1) <-> right 
    left <-> (2,2) <-> (1,1) <-> (3,3) <-> right 
    '''
    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
'''
left <-> (2,2) <-> (1,1) <-> (3,3) <-> right 
left <-> (1,1) <-> (3,3) <-> right 
'''

'''
left(-1) <-> right(-1) , cap = 2

left <-> (1,1) <-> right  
cache = {1:(1,1)}

insert, remove in double linked list, also need to handle cache

left <-> (1,1) <-> (2,2) <-> right
cache = {1:(1,1), 2:(2,2)}

left <-> (2,2) <-> (1,1) <-> right
cache = {1:(1,1), 2:(2,2)}
if get(1) -> remove(1,1) -> insert(1, 1)

left <-> (2,2) <-> (1,1) <-> (3,3) <-> right
left <-> (1,1) <-> (3,3) <-> right
cache = {1:(1,1), 3:(3,3)}

2 is not in cache, return -1

left <-> (1,1) <-> (3,3) <-> (4,4) <-> right
left <-> (3,3) <-> (4,4) <-> right
cache = {3:(3,3), 4:(4,4)}
'''


class LRUCache:

    def __init__(self, capacity: int):
        self.cacheDict = OrderedDict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.cacheDict:
            self.cacheDict.move_to_end(key)
            return self.cacheDict[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cacheDict:
            self.cacheDict.move_to_end(key)
        self.cacheDict[key] = value
        if len(self.cacheDict) > self.capacity:
            self.cacheDict.popitem(last = False)
        



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
