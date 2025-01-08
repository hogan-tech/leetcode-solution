# time complexity: O(n)
# space complexity: O(1)
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        successor = None
        while root:
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right
        return successor


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
p = TreeNode(1)
print(Solution().inorderSuccessor(root, p))
