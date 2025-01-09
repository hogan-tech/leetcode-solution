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
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return False
        remainSet = set()
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node:
                if k - node.val in remainSet:
                    return True
                remainSet.add(node.val)
                queue.append(node.left)
                queue.append(node.right)

        return False


root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.right = TreeNode(6)
root1.left.left = TreeNode(2)
root1.left.right = TreeNode(4)
root1.right.right = TreeNode(7)
k = 9
print(Solution().findTarget(root1, 9))
root2 = TreeNode(5)
root2.left = TreeNode(3)
root2.right = TreeNode(6)
root2.left.left = TreeNode(2)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)
k = 28
print(Solution().findTarget(root2, 28))
