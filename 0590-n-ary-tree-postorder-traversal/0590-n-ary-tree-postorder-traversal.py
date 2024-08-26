# time complexity: O(m)
# space complexity: O(m)
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: "Node") -> List[int]:
        result = []
        if root is None:
            return result
        nodeStack = [root]
        while nodeStack:
            currentNode = nodeStack.pop()
            result.append(currentNode.val)
            for child in currentNode.children:
                nodeStack.append(child)

        result.reverse()
        return result


root = Node(1)
root.children = Node(3)
root.children.children = Node(5)
root.children.children = Node(6)
root.children = Node(2)
root.children = Node(4)
