# time complexity: O(n)
# space complexity: O(n)
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxWidth = 0
        queue = deque()
        queue.append((root, 0))
        while queue:
            queLen = len(queue)
            _, headIdx = queue[0]
            for _ in range(queLen):
                node, colIdx = queue.popleft()
                if node.left:
                    queue.append((node.left, colIdx * 2))
                if node.right:
                    queue.append((node.right, colIdx * 2 + 1))
            maxWidth = max(maxWidth, colIdx - headIdx + 1)
        return maxWidth


root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)
print(Solution().widthOfBinaryTree(root))
