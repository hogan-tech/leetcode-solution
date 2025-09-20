# time complexity: O(n)
# space complexity: O(1)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        leftTail = self.flatten(root.left)
        rightRail = self.flatten(root.right)
        if leftTail:
            leftTail.right = root.right
            root.right = root.left
            root.left = None
        return rightRail if rightRail else leftTail

# time complexity: O(n)
# space complexity: O(1)
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
