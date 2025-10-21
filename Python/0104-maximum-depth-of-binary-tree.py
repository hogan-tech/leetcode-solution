# time complexity: O(n)
# space complexity: O(logn)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def longestPath(node: Optional[TreeNode]):
            if not node:
                return 0
            leftPath = longestPath(node.left)
            rightPath = longestPath(node.right)
            return max(leftPath, rightPath)+1
        return longestPath(root)


# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def __init__(self):
        self.nextItem = []
        self.maxDepth = 0

    def nextMaxDepth(self):
        if not self.nextItem:
            return self.maxDepth
        nextNode, nextLvl = self.nextItem.pop(0)
        nextLvl += 1
        self.maxDepth = max(self.maxDepth, nextLvl)
        if nextNode.left:
            self.nextItem.append((nextNode.left, nextLvl))
        if nextNode.right:
            self.nextItem.append((nextNode.right, nextLvl))
        return self.nextMaxDepth()

    def maxDepth(self, root):
        if not root:
            return 0
        self.nextItem = []
        self.maxDepth = 0
        self.nextItem.append((root, 0))
        return self.nextMaxDepth()

# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0
        while stack != []:
            currDepth, root = stack.pop()
            if root is not None:
                depth = max(depth, currDepth)
                stack.append((currDepth + 1, root.left))
                stack.append((currDepth + 1, root.right))

        return depth
