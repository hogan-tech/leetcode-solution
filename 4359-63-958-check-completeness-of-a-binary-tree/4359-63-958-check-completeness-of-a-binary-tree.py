# time complexity: O(n)
# space complexity: O(n)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def countNode(node: Optional[TreeNode]):
            if node is None:
                return 0
            return 1 + countNode(node.left) + countNode(node.right)

        def dfs(node: Optional[TreeNode], index: int, n: int):
            if node is None:
                return True
            if index >= n:
                return False
            return dfs(node.left, 2 * index + 1, n) and dfs(node.right, 2 * index + 2, n)

        return dfs(root, 0, countNode(root))


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.right.left = TreeNode(6)
print(Solution().isCompleteTree(root1))
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.right.right = TreeNode(7)
print(Solution().isCompleteTree(root2))
