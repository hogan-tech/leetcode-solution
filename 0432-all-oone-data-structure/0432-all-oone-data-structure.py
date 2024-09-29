class Node:
    def __init__(self, freq):
        self.freq = freq
        self.prev = None
        self.next = None
        self.keys = set()


class AllOne:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}

    def inc(self, key: str) -> None:
        if key in self.map:
            node = self.map[key]
            freq = node.freq
            node.keys.remove(key)

            nextNode = node.next
            if nextNode == self.tail or nextNode.freq != freq + 1:

                newNode = Node(freq + 1)
                newNode.keys.add(key)
                newNode.prev = node
                newNode.next = nextNode
                node.next = newNode
                nextNode.prev = newNode
                self.map[key] = newNode
            else:

                nextNode.keys.add(key)
                self.map[key] = nextNode

            if not node.keys:
                self.removeNode(node)
        else:
            firstNode = self.head.next
            if firstNode == self.tail or firstNode.freq > 1:

                newNode = Node(1)
                newNode.keys.add(key)
                newNode.prev = self.head
                newNode.next = firstNode
                self.head.next = newNode
                firstNode.prev = newNode
                self.map[key] = newNode
            else:
                firstNode.keys.add(key)
                self.map[key] = firstNode

    def dec(self, key: str) -> None:
        if key not in self.map:
            return

        node = self.map[key]
        node.keys.remove(key)
        freq = node.freq

        if freq == 1:

            del self.map[key]
        else:
            prevNode = node.prev
            if prevNode == self.head or prevNode.freq != freq - 1:

                newNode = Node(freq - 1)
                newNode.keys.add(key)
                newNode.prev = prevNode
                newNode.next = node
                prevNode.next = newNode
                node.prev = newNode
                self.map[key] = newNode
            else:

                prevNode.keys.add(key)
                self.map[key] = prevNode

        if not node.keys:
            self.removeNode(node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(
            iter(self.tail.prev.keys)
        )

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(
            iter(self.head.next.keys)
        )

    def removeNode(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode


allOne = AllOne()
print(allOne.inc("hello"))
print(allOne.inc("hello"))
print(allOne.getMaxKey())
print(allOne.getMinKey())
print(allOne.inc("leet"))
print(allOne.getMaxKey())
print(allOne.getMinKey())
