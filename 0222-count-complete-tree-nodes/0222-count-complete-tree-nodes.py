from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        counter = 0
        def traverse(node: Optional[TreeNode]):
            nonlocal counter
            if node is None:
                return
            counter += 1
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return counter



root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
print(Solution().countNodes(root))