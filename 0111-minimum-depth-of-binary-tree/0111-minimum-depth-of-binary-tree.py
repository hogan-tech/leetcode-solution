
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        level = 0
        minLevel = 100000
        if root is None:
            return 0
        while q:
            level += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node is None:
                    break
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if node.left is None and node.right is None:
                    minLevel = min(minLevel, level)
        return minLevel


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().minDepth(root))
