# time complexity: O(n)
# space compelexity: O(n)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        result = []

        def levelOrder(node, level):
            if not node:
                return None
            if len(result) == level:
                result.append([])
            result[level].append(node.val)
            if node.left:
                levelOrder(node.left, level + 1)
            if node.right:
                levelOrder(node.right, level + 1)

        levelOrder(root, 0)
        return sum(result[-1])


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.left.left = TreeNode(7)
root.right.right.right = TreeNode(8)
print(Solution().deepestLeavesSum(root))
