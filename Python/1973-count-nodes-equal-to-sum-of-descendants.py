# time complexity: O(n)
# space complexity: O(n)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        count = 0

        def countNodes(node: Optional[TreeNode]) -> int:
            nonlocal count
            if node == None:
                return 0
            left = countNodes(node.left)
            right = countNodes(node.right)
            if left + right == node.val:
                count += 1
            return node.val + left + right

        countNodes(root)
        return count


root = TreeNode(10)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(1)
root.right = TreeNode(4)

print(Solution().equalToDescendants(root))
