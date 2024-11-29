# time complexity: O(n)
# space complexity: O(1)
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:

    def processChild(self, childNode, prev, leftmost):
        if childNode:

            if prev:
                prev.next = childNode
            else:
                leftmost = childNode
            prev = childNode
        return prev, leftmost

    def connect(self, root: Optional["Node"]) -> Optional["Node"]:
        if not root:
            return root
        leftmost = root

        while leftmost:
            prev, curr = None, leftmost
            leftmost = None

            while curr:
                prev, leftmost = self.processChild(curr.left, prev, leftmost)
                prev, leftmost = self.processChild(curr.right, prev, leftmost)
                curr = curr.next

        return root


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.right = Node(7)
print(Solution().connect(root))
