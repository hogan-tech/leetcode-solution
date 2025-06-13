# time complexity: O(n + m)
# space complexity: O(n)
from collections import deque
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        if node in self.visited:
            return self.visited[node]

        cloneNode = Node(node.val, [])
        self.visited[node] = cloneNode

        if node.neighbors:
            cloneNode.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return cloneNode


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        visited = {}
        queue = deque()
        queue.append(node)
        visited[node] = Node(node.val, [])

        while queue:
            currNode = queue.popleft()
            for nextNode in currNode.neighbors:
                if nextNode not in visited:
                    visited[nextNode] = Node(nextNode.val, [])
                    queue.append(nextNode)

                visited[currNode].neighbors.append(visited[nextNode])

        return visited[node]
