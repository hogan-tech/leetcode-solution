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
        maxPath = float('-inf')

        def dfs(node: Optional[TreeNode]):
            nonlocal maxPath
            if node is None:
                return 0
            pathLeft = max(dfs(node.left), 0)
            pathRight = max(dfs(node.right), 0)
            maxPath = max(maxPath, pathLeft + pathRight + node.val)
            return max(pathLeft + node.val, pathRight + node.val)
        dfs(root)
        return maxPath


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(Solution().maxPathSum(root))
