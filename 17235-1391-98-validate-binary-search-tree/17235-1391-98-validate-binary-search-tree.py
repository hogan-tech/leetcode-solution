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
        def dfs(node: Optional[TreeNode], low=-math.inf, high=math.inf):
            if node is None:
                return True
            if node.val <= low:
                return False
            if node.val >= high:
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        return dfs(root)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = [-math.inf]

        def dfs(node: Optional[TreeNode], prev):
            if not node:
                return True
            if not dfs(node.left, prev):
                return False
            if node.val <= prev[0]:
                return False
            prev[0] = node.val
            return dfs(node.right, prev)
        
        return dfs(root, prev)


root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)
print(Solution().isValidBST(root1))
root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(6)
print(Solution().isValidBST(root2))
