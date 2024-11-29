# time complexixty: O(n)
# space complexity: O(n)
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root: Optional[TreeNode], low=-math.inf, high=math.inf):
            if not root:
                return True
            if root.val <= low:
                return False
            if root.val >= high:
                return False
            return helper(root.left, low, root.val) and helper(root.right, root.val, high)

        return helper(root)
