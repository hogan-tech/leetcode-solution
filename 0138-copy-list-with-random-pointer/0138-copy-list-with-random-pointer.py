# time complexity: O(n)
# space complexity: O(n)
from typing import Optional


def buildLinkedList(arr):
    if not arr:
        return None

    nodes = [Node(val) for val, _ in arr]
    for i, (_, randIdx) in enumerate(arr):
        if i < len(nodes) - 1:
            nodes[i].next = nodes[i + 1]
        if randIdx is not None:
            nodes[i].random = nodes[randIdx]
    return nodes[0]


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution():
    def __init__(self):
        self.visited = {}

    def copyRandomList(self, head: Optional[Node]):

        if head == None:
            return None

        if head in self.visited:
            return self.visited[head]

        node = Node(head.val, None, None)

        self.visited[head] = node

        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node


head1 = buildLinkedList([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
print(Solution().copyRandomList(head1))

head2 = buildLinkedList([[1, 1], [2, 1]])
print(Solution().copyRandomList(head2))

head3 = buildLinkedList([[3, None], [3, 0], [3, None]])
print(Solution().copyRandomList(head3))

head4 = buildLinkedList([])
print(Solution().copyRandomList(head4))
