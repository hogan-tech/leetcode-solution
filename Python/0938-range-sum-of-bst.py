# time complexity: O(n)
# space complexity: O(n)
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        SumBST = 0

        def preorder(node: Optional[TreeNode]):
            nonlocal SumBST
            if node:
                if low <= node.val <= high:
                    SumBST += node.val
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        return SumBST


root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right = TreeNode(15)
root.right.right = TreeNode(18)

low = 7
high = 15

print(Solution().rangeSumBST(root, low, high))
