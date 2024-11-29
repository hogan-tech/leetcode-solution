# time complexity: O(n)
# space complexity: O(n)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        count = 0

        def traverse(node: TreeNode, goLeft: bool, steps: int):
            nonlocal count
            if node is None:
                return
            count = max(count, steps)
            if goLeft:
                traverse(node.left, False, steps + 1)
                traverse(node.right, True, 1)
            else:
                traverse(node.left, False, 1)
                traverse(node.right, True, steps + 1)

        traverse(root, False, 0)
        traverse(root, True, 0)
        return count


root = TreeNode(1)
root.right = TreeNode(1)
root.right.left = TreeNode(1)
root.right.right = TreeNode(1)
root.right.right.left = TreeNode(1)
root.right.right.left.right = TreeNode(1)
root.right.right.left.right.right = TreeNode(1)
root.right.right.right = TreeNode(1)
print(Solution().longestZigZag(root))
