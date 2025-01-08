# time complexity: O(n)
# space complexity: O(1)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flattenTree(self, node: TreeNode) -> TreeNode:
        if node is None:
            return None
        if node.left is None and node.right is None:
            return node
        leftTail = self.flattenTree(node.left)
        rightRail = self.flattenTree(node.right)

        if leftTail:
            leftTail.right = node.right
            node.right = node.left
            node.left = None

        return rightRail if rightRail else leftTail

    def flatten(self, root: Optional[TreeNode]) -> None:
        self.flattenTree(root)


class Solution:
    def flatten(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        current = root
        while current:
            if current.left:
                last = current.left
                while last.right:
                    last = last.right
                last.right = current.right
                current.right = current.left
                current.left = None

            current = current.right

        return root


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(5)
root.right.right = TreeNode(6)
print(Solution().flatten(root))
