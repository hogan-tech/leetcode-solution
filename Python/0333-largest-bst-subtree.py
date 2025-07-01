# time complexity: O(n^2)
# space complexity: O(n)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValid(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if not self.isValid(root.left):
            return False
        if self.previous and self.previous.val >= root.val:
            return False
        self.previous = root
        return self.isValid(root.right)

    def countNode(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + self.countNode(root.left) + self.countNode(root.right)

    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.previous = None
        if self.isValid(root):
            return self.countNode(root)
        return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(1)
root.left.right = TreeNode(8)
root.right.right = TreeNode(7)
print(Solution().largestBSTSubtree(root))
