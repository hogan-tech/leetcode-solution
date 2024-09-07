# time complexity: O(n)
# space complexity: O(n)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = -float("inf")

        def gainFromSubTree(node: Optional[TreeNode]) -> int:
            nonlocal maxPath
            if node is None:
                return 0
            gainLeft = max(gainFromSubTree(node.left), 0)
            gainRight = max(gainFromSubTree(node.right), 0)
            maxPath = max(gainLeft + gainRight + node.val, maxPath)
            return max(gainLeft + node.val, gainRight + node.val)

        gainFromSubTree(root)
        return maxPath


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(Solution().maxPathSum(root))
