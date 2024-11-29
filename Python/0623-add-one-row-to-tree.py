# time complexity: O(n)
# space complexity: O(n)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def add(self, root: Optional[TreeNode], val: int, depth: int, curr: int):
        if not root:
            return None
        if curr == depth - 1:
            lTemp = root.left
            rTemp = root.right

            root.left = TreeNode(val)
            root.right = TreeNode(val)
            root.left.left = lTemp
            root.right.right = rTemp

            return root

        root.left = self.add(root.left, val, depth, curr+1)
        root.right = self.add(root.right, val, depth, curr+1)
        return root

    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot
        return self.add(root, val, depth, 1)


root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(6)
root.left.right = TreeNode(3)
root.right = TreeNode(1)
root.right.left = TreeNode(5)
val = 1
depth = 2
print(Solution().addOneRow(root, val, depth))
