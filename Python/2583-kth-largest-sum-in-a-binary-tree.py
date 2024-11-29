from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        levels = []
        if root is None:
            return

        def traverse(node: Optional[TreeNode], level: int):
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            if node.left:
                traverse(node.left, level + 1)
            if node.right:
                traverse(node.right, level + 1)
        traverse(root, 0)
        for i in range(len(levels)):
            levels[i] = sum(levels[i])
        levels.sort(reverse=True)

        return levels[k-1] if len(levels) >= k else -1


root = TreeNode(5)
root.left = TreeNode(8)
root.right = TreeNode(9)
root.left.left = TreeNode(2)
root.left.right = TreeNode(1)
root.right.left = TreeNode(3)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(6)
k = 4
print(Solution().kthLargestLevelSum(root, k))
