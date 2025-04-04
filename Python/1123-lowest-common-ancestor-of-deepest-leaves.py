# time complexity: O(n)
# space complexity: O(n)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node, depth):
            if not node:
                return (None, depth)
            leftLca, leftDepth = dfs(node.left, depth + 1)
            rightLca, rightDepth = dfs(node.right, depth + 1)
            if leftDepth > rightDepth:
                return (leftLca, leftDepth)
            elif rightDepth > leftDepth:
                return (rightLca, rightDepth)
            else:
                return (node, leftDepth)

        lcaNode, _ = dfs(root, 0)
        return lcaNode


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
print(Solution().lcaDeepestLeaves(root))
