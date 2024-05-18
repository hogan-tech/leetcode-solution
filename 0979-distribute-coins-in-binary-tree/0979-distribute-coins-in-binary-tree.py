# time complexity: O(n)
# space complexity: O(n)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0

        def dfs(node: Optional[TreeNode]):
            if not node:
                return 0
            leftBal = dfs(node.left)
            rightBal = dfs(node.right)
            self.moves += abs(leftBal) + abs(rightBal)
            return node.val + leftBal + rightBal - 1
        dfs(root)
        return self.moves


root = TreeNode(3)
root.left = TreeNode(0)
root.right = TreeNode(0)
print(Solution().distributeCoins(root))
