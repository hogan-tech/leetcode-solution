# time complexity: O(h)
# space complexity; O(h)
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        if root is None:
            return [None, None]
        if root.val > target:
            left = self.splitBST(root.left, target)
            root.left = left[1]
            return [left[0], root]
        else:
            right = self.splitBST(root.right, target)
            root.right = right[0]
            return [root, right[1]]


root = TreeNode(2)
root.left = TreeNode(4)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(6)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
target = 2
print(Solution().splitBST(root, target))
