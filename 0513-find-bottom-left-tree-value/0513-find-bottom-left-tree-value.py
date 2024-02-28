# time complexity: O(n)
# space complexity: O(n)
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        current = root
        queue.append(current)

        while queue:
            current = queue.popleft()
            if current.right:
                queue.append(current.right)
            if current.left:
                queue.append(current.left)

        return current.val


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.left.right = TreeNode(7)
root.right.right = TreeNode(6)
print(Solution().findBottomLeftValue(root))
