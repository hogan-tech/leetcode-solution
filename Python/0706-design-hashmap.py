# time complexity: O(1) average per operation, O(n) worst-case
# space complexity: O(N)
from collections import defaultdict
# Bucket
class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break

        if not found:
            self.bucket.append((key, value))

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]


class MyHashMap(object):

    def __init__(self):
        self.keySpace = 2068
        self.hashTable = [Bucket() for _ in range(self.keySpace)]


    def put(self, key, value):
        hashKey = key % self.keySpace
        self.hashTable[hashKey].update(key, value)
        


    def get(self, key):
        hashKey = key % self.keySpace
        return self.hashTable[hashKey].get(key)


    def remove(self, key):
        hashKey = key % self.keySpace
        self.hashTable[hashKey].remove(key)


# Linked List
class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:
    def __init__(self):
        self.map = [ListNode() for _ in range(1000)]

    def hash(self, key):
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        cur = self.map[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        cur = self.map[self.hash(key)].next
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.map[self.hash(key)]
        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

# HashMap
class MyHashMap:

    def __init__(self):
        self.hashMap = defaultdict(int)

    def put(self, key: int, value: int) -> None:
        self.hashMap[key] = value
        

    def get(self, key: int) -> int:
        if key not in self.hashMap:
            return -1
        else:
            return self.hashMap[key]
        

    def remove(self, key: int) -> None:
        if key in self.hashMap:
            del self.hashMap[key]

obj = MyHashMap()
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
print(obj.get(2))
print(obj.get(3))
obj.put(2, 1)
print(obj.get(2))
obj.remove(2)
print(obj.get(2))
