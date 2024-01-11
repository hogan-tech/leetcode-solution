# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def helper(node: Optional[TreeNode], currMax: int, currMin: int):
            if not node:
                return
            self.result = max(self.result, abs(
                node.val - currMax), abs(node.val - currMin))
            currMax = max(currMax, node.val)
            currMin = min(currMin, node.val)
            helper(node.left, currMax, currMin)
            helper(node.right, currMax, currMin)

        helper(root, root.val, root.val)
        return self.result


root = TreeNode(8)
root.left = TreeNode(3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right = TreeNode(10)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)

print(Solution().maxAncestorDiff(root))
