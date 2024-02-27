# time complexity: O(n)
# space complexity: O(n)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def longestPath(node: Optional[TreeNode]):
            if not node:
                return 0
            nonlocal diameter
            leftPath = longestPath(node.left)
            rightPath = longestPath(node.right)
            diameter = max(diameter, leftPath + rightPath)
            return max(leftPath, rightPath) + 1

        longestPath(root)
        return diameter


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
