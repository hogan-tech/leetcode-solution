# time complexity: O(n)
# space complexity: O(n)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return root.val != 0
        evalRootLeft = self.evaluateTree(root.left)
        evalRootRight = self.evaluateTree(root.right)

        if root.val == 2:
            evalRoot = evalRootLeft or evalRootRight
        else:
            evalRoot = evalRootLeft and evalRootRight
        return evalRoot


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)
print(Solution().evaluateTree(root))
