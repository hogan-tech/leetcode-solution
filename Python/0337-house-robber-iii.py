# time complexity: O(n)
# space complexity: O(n)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def backtrack(node: Optional[TreeNode]):
            if node is None:
                return [0, 0]
            leftSubtree = backtrack(node.left)
            rightSubtree = backtrack(node.right)
            includeRoot = node.val + leftSubtree[1] + rightSubtree[1]
            excludeRoot = max(leftSubtree) + max(rightSubtree)
            return [includeRoot, excludeRoot]
        return max(backtrack(root))


root1 = TreeNode(3)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.right = TreeNode(3)
root1.right.right = TreeNode(1)
print(Solution().rob(root1))
root2 = TreeNode(3)
root2.left = TreeNode(4)
root2.right = TreeNode(5)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(3)
root2.right.right = TreeNode(1)
print(Solution().rob(root2))
