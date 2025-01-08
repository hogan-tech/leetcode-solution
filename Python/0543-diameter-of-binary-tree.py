# time complexity: O(n)
# space complexity: O(n)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(node: Optional[TreeNode]):
            nonlocal result
            if node is None:
                return 0
            leftResult = dfs(node.left)
            rightResult = dfs(node.right)
            result = max(result, leftResult + rightResult)
            return max(leftResult, rightResult) + 1
        dfs(root)
        return result


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
print(Solution().diameterOfBinaryTree(root))
