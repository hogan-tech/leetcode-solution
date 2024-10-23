from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        cousinDict = defaultdict(tuple)

        if not root:
            return

        def traverse(node: Optional[TreeNode], level: int, parentVal: int):
            if node.val:
                cousinDict[node.val] = (level, parentVal)
            if node.left:
                traverse(node.left, level + 1, node.val)
            if node.right:
                traverse(node.right, level + 1, node.val)

        traverse(root, 0, float('inf'))
        return cousinDict[x][0] == cousinDict[y][0] and cousinDict[x][1] != cousinDict[y][1]


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
x = 4
y = 3
print(Solution().isCousins(root, x, y))
