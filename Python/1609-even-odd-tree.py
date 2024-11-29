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
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = deque([root])
        level = 0

        while queue:
            prevVal = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if (level % 2 == 0 and (node.val % 2 == 0 or (prevVal is not None and node.val <= prevVal))) or \
                        (level % 2 == 1 and (node.val % 2 == 1 or (prevVal is not None and node.val >= prevVal))):
                    return False
                prevVal = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return True


root = TreeNode(1)
root.left = TreeNode(10)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(12)
root.left.left.right = TreeNode(8)
root.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.left.left = TreeNode(6)
root.right.right = TreeNode(9)
root.right.right.right = TreeNode(2)
print(Solution().isEvenOddTree(root))
